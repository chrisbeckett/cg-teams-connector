# CloudGuard Microsoft Teams Connector

## What does it do?

This connector runs as an Azure Function and provides a webhook URL for CloudGuard (formerly Dome9) to send alerts to. This provides simple connectivity to Microsoft Teams as it sends alert information as cards into a Teams channel.

![alt text](https://github.com/chrisbeckett/dome9-teams-connector/blob/master/teams-connector.png "Teams screenshot")

## How does it work?

CloudGuard runs regular compliance checks ("Continuous Compliance") and any *new* findings are sent as alerts to destinations determined by the compliance policy. In this case, you add a notification configuration and add the webhook URL of the Azure Function as the destination. This sends a JSON payload with the finding details and the Azure Function turns this information into a Teams card and sends it to Teams Webhook.

![alt text](https://github.com/chrisbeckett/dome9-teams-connector/blob/master/teams-connector-architecture.png "Architecture overview")

## What do I need to get started?

* A CloudGuard tenant (duh)
* An onboarded cloud account or two
* Continuous Compliance configured
* A Microsoft Teams account (double duh)
* A Teams channel to send alerts to
* A Teams webhook URL (https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook)
* Python 3.7
* Git

## Obtaining the code

Run **git clone https://github.com/chrisbeckett/dome9-teams-connector.git**

## Deploying the Azure Function

Click the "Deploy to Azure" button and fill out the deployment form
- Both the **Azure Function** name and the **Storage Account** name **must be globally unique or deployment will fail (if a new storage account is created)**
- Once the ARM template deployment is complete, open a command prompt and navigate to the **dome9-teams-connector** folder
- Install the Azure Functions command line tools (*https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Ccsharp%2Cbash*)
- Run **func init**
- Run **func azure functionapp publish *functname*** where the functname is your function name from the "**Deploy to Azure**" workflow
- When this is complete, you will need the HTTP trigger URL (Function overview, "Get Function URL" button)
- When you create the notification in CloudGuard, set the function trigger URL as the Endpoint URL in the "Send to HTTP Endpoint", click "Test" to make sure it is working 
- Create/configure a Compliance Policy and add the HTTP Endpoint you defined earlier as the notification target
- To test the integration, go into Compliance Policies, find the appopriate ruleset and click the "Send All Alerts" icon on the right hand side (up arrow icon), select Notification Type as Webhook and Notification as the Teams Connector Webhook URL from Azure Functions

[![Deploy to Azure](https://azuredeploy.net/deploybutton.png)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fchrisbeckett%2Fdome9-teams-connector%2Fmaster%2Fdeployment-template.json)
