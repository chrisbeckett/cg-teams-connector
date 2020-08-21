# CloudGuard Microsoft Teams Connector

## What does it do?

This connector runs as an Azure Function and provides a webhook URL for CloudGuard (formerly Dome9) to send alerts to. This provides simple connectivity to Microsoft Teams as it sends alert information as cards into a Teams channel.

![alt text](https://github.com/chrisbeckett/dome9-teams-connector/blob/master/teams-connector.png "Teams screenshot")


## What do I need to get started?

* A CloudGuard tenant (duh)
* An onboarded cloud account or two
* Continuous Compliance configured
* A Microsoft Teams account (double duh)
* A teams channel to send alerts to
* Python 3.7
* Git

## Obtaining the code

Run **git clone https://github.com/chrisbeckett/dome9-teams-connector.git**

## Deploying the Azure Function

Click the button below and follow the prompts. Easy peasy.

[![Deploy to Azure](https://azuredeploy.net/deploybutton.png)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fchrisbeckett%2Fdome9-teams-connector%2Fmaster%2Fdeployment-template.json
