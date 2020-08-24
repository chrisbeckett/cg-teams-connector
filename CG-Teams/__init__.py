import logging
import azure.functions as func
import json
import pymsteams
import os
import dateutil.parser

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('CloudGuard Microsoft Teams Connector HTTP trigger function processed a request.')
    logging.info('Code version : 24082020-1009 - fixed typo in alert ext in card')
    try:
        source_message = req.get_json()
        logging.info(f'Finding alert message content is - {source_message}')
        if source_message:
            teams_webhook_url = os.getenv('TEAMS_WEBHOOK_URL')
            logging.info(f'Teams webhook URL set to {teams_webhook_url}')
            ruleset_name = source_message.get('bundle', {}).get('name')
            ruleset_description = source_message.get('bundle', {}).get('description')
            ruleset_account = source_message.get('account', {}).get('name')
            ruleset_platform = source_message.get('account', {}).get('vendor')
            rule_name = source_message.get('rule', {}).get('name')
            rule_description = source_message.get('rule', {}).get('description')
            rule_severity = source_message.get('rule', {}).get('severity')
            finding_id = source_message.get('findingKey')
            finding_timestamp = source_message.get('reportTime')
            entity_name = source_message.get('entity', {}).get('id')
            formatted_timestamp = dateutil.parser.parse(finding_timestamp)
            display_timestamp = formatted_timestamp.ctime()
            review_findings_url = "https://secure.dome9.com/v2/alerts/findings"

            logging.info(f'Building Teams message card...')
            teams_message = pymsteams.connectorcard(teams_webhook_url)
            teams_message.text("CloudGuard has detected a new " + rule_severity + " severity finding")
            teams_message.title("CloudGuard - Alert Notification")    
            teams_message.addLinkButton("Review latest alerts", review_findings_url)
            teams_message.color("ff7474")
            teams_message_section = pymsteams.cardsection()
            teams_message_section.activityImage("https://beckettdiags.blob.core.windows.net/web/circle-cropped.png")
            teams_message_section.title("Alert Information")
            teams_message_section.addFact("Ruleset Name: ", ruleset_name)
            teams_message_section.addFact("Ruleset Description: ", ruleset_description)
            teams_message_section.addFact("Cloud Platform / Account: ", ruleset_platform + " - " + ruleset_account)
            teams_message_section.addFact("Rule Name: ", rule_name)
            teams_message_section.addFact("Rule Description: ", rule_description)
            teams_message_section.addFact("Rule Severity: ", rule_severity)
            teams_message_section.addFact("Alert ID / Date: ", finding_id + " - " + display_timestamp)
            teams_message_section.addFact("Entity ID: ", entity_name)
            teams_message.addSection(teams_message_section)
            logging.info(f'Sending Teams message card...')
            teams_message.send()
            msg="Operation complete - Teams message successful"
            logging.info(f'{msg}')
            return func.HttpResponse(status_code=200)

    except Exception as e:
            logging.info(f'Bad request. {e}')
            return func.HttpResponse(status_code=400)
            
