# Microsoft Teams connector for Dome9
# Feedback to chrisbe@checkpoint.com

import json
import requests
import pymsteams


# payload = {
# 	"status": "Failed",
# 	"policy": {
# 		"name": "Webhook.site",
# 		"description": "Dump payload into webhook site for analysis"
# 	},
# 	"findingKey": "fLAzyXtk5/oAfjq9aDBxBg",
# 	"bundle": {
# 		"name": "MS Ignite The Tour",
# 		"description": "Custom checks for MITT 2019",
# 		"id": 45772
# 	},
# 	"reportTime": "2020-08-18T12:26:04.298Z",
# 	"rule": {
# 		"name": "Tags – Check Tag Values e.g. Value should be in certain format e.g. ??##### (2 Letters – AL and 5 numbers) and length should be 7 characters",
# 		"ruleId": "",
# 		"description": "Check all cloud resources are tagged with the corporate standard tagging convention (AA12345)",
# 		"remediation": "- Add tags to missing objects\n- Snitch on resource owner to the CISO",
# 		"complianceTags": "",
# 		"logicHash": "uA/UMGRLGAGFYCpzEKJvaw",
# 		"severity": "High"
# 	},
# 	"account": {
# 		"id": "e584d070-3c5a-4a7c-8cf9-c063c5c67ee3",
# 		"name": "Azure-Prod",
# 		"vendor": "Azure",
# 		"dome9CloudAccountId": "0bd33263-9978-45fb-b2b8-3df69b721a3e",
# 		"organizationalUnitId": "00000000-0000-0000-0000-000000000000",
# 		"organizationalUnitPath": ""
# 	},
# 	"region": "North Europe",
# 	"entity": {
# 		"machineImage": {
# 			"offer": "azure-vms-by-zerto",
# 			"publisher": "zerto",
# 			"sku": "ubuntu1804lts-python-docker-zerto",
# 			"version": "1.0.0"
# 		},
# 		"resourceGroup": {
# 			"locks": None,
# 			"id": "/subscriptions/e584d070-3c5a-4a7c-8cf9-c063c5c67ee3/resourceGroups/rg-jenkins",
# 			"type": "ResourceGroup",
# 			"name": "rg-jenkins",
# 			"dome9Id": "7|0bd33263-9978-45fb-b2b8-3df69b721a3e|resourcegroup|rg-jenkins",
# 			"accountNumber": "e584d070-3c5a-4a7c-8cf9-c063c5c67ee3",
# 			"region": "uksouth",
# 			"source": "db",
# 			"tags": [],
# 			"externalFindings": None
# 		},
# 		"size": "Standard_D1_v2",
# 		"operatingSystem": "Linux",
# 		"virtualHardDisk": None,
# 		"availabilitySet": None,
# 		"nics": [
# 			{
# 				"id": "/subscriptions/e584d070-3c5a-4a7c-8cf9-c063c5c67ee3/resourceGroups/rg-jenkins/providers/Microsoft.Network/networkInterfaces/jenkins346",
# 				"name": "jenkins346",
# 				"tags": {},
# 				"resourceGroup": {
# 					"locks": None,
# 					"id": "/subscriptions/e584d070-3c5a-4a7c-8cf9-c063c5c67ee3/resourceGroups/rg-jenkins",
# 					"type": "ResourceGroup",
# 					"name": "rg-jenkins",
# 					"dome9Id": "7|0bd33263-9978-45fb-b2b8-3df69b721a3e|resourcegroup|rg-jenkins",
# 					"accountNumber": "e584d070-3c5a-4a7c-8cf9-c063c5c67ee3",
# 					"region": "uksouth",
# 					"source": "db",
# 					"tags": [],
# 					"externalFindings": None
# 				},
# 				"region": "northeurope",
# 				"enableIpForwarding": """""false""""",
# 				"primary": "true",
# 				"macAddress": "00-0D-3A-BA-96-25",
# 				"etag": "W/\"de419f17-2170-43e0-b218-176a1ca49527\"",
# 				"networkSecurityGroup": {
# 					"resourceGroup": {
# 						"locks": None,
# 						"id": "/subscriptions/e584d070-3c5a-4a7c-8cf9-c063c5c67ee3/resourceGroups/rg-jenkins",
# 						"type": "ResourceGroup",
# 						"name": "rg-jenkins",
# 						"dome9Id": "7|0bd33263-9978-45fb-b2b8-3df69b721a3e|resourcegroup|rg-jenkins",
# 						"accountNumber": "e584d070-3c5a-4a7c-8cf9-c063c5c67ee3",
# 						"region": "uksouth",
# 						"source": "db",
# 						"tags": [],
# 						"externalFindings": None
# 					},
# 					"etag": "W/\"417d46ca-0dea-4509-b3a7-203921edc4a1\"",
# 					"networkAssetsStats": [],
# 					"id": "/subscriptions/e584d070-3c5a-4a7c-8cf9-c063c5c67ee3/resourcegroups/rg-jenkins/providers/microsoft.network/networksecuritygroups/jenkins-nsg",
# 					"type": "NetworkSecurityGroup",
# 					"name": "jenkins-nsg",
# 					"dome9Id": "7|0bd33263-9978-45fb-b2b8-3df69b721a3e|resourcegroup|rg-jenkins|securitygroup|jenkins-nsg",
# 					"accountNumber": "e584d070-3c5a-4a7c-8cf9-c063c5c67ee3",
# 					"region": "northeurope",
# 					"source": "db",
# 					"tags": []
# 				},
# 				"ipConfigurations": [
# 					{
# 						"name": "ipconfig1",
# 						"primary": "true",
# 						"publicIpAddress": "",
# 						"publicIpAllocationMethod": "Dynamic",
# 						"publicIpAddressVersion": "IPv4",
# 						"privateIpAddress": "10.0.2.4",
# 						"resourceUri": "/subscriptions/e584d070-3c5a-4a7c-8cf9-c063c5c67ee3/resourceGroups/rg-jenkins/providers/Microsoft.Network/networkInterfaces/jenkins346/ipConfigurations/ipconfig1",
# 						"subnetId": "/subscriptions/e584d070-3c5a-4a7c-8cf9-c063c5c67ee3/resourceGroups/rg-networking/providers/Microsoft.Network/virtualNetworks/vnet-cplab/subnets/External",
# 						"applicationSecurityGroups": []
# 					}
# 				],
# 				"subnet": {
# 					"routeTable": None,
# 					"securityGroup": {
# 						"inboundRules": [
# 							{
# 								"sourceApplicationSecurityGroups": None,
# 								"destinationApplicationSecurityGroups": None,
# 								"name": "Any",
# 								"number": 100,
# 								"protocol": "All",
# 								"source": "0.0.0.0/0",
# 								"destination": "0.0.0.0/0",
# 								"destinationPort": 0,
# 								"destinationPortTo": 65535,
# 								"direction": "INBOUND",
# 								"action": "ALLOW"
# 							}
# 						],
# 						"outboundRules": [],
# 						"defaultInboundRules": [
# 							{
# 								"sourceApplicationSecurityGroups": None,
# 								"destinationApplicationSecurityGroups": None,
# 								"name": "AllowVnetInBound",
# 								"number": 65000,
# 								"protocol": "All",
# 								"source": "10.0.0.0/16",
# 								"destination": "10.0.0.0/16",
# 								"destinationPort": 0,
# 								"destinationPortTo": 65535,
# 								"direction": "INBOUND",
# 								"action": "ALLOW"
# 							},
# 							{
# 								"sourceApplicationSecurityGroups": None,
# 								"destinationApplicationSecurityGroups": None,
# 								"name": "AllowAzureLoadBalancerInBound",
# 								"number": 65001,
# 								"protocol": "All",
# 								"source": "NOT-SUPPORTED",
# 								"destination": "0.0.0.0/0",
# 								"destinationPort": 0,
# 								"destinationPortTo": 65535,
# 								"direction": "INBOUND",
# 								"action": "ALLOW"
# 							},
# 							{
# 								"sourceApplicationSecurityGroups": None,
# 								"destinationApplicationSecurityGroups": None,
# 								"name": "DenyAllInBound",
# 								"number": 65500,
# 								"protocol": "All",
# 								"source": "0.0.0.0/0",
# 								"destination": "0.0.0.0/0",
# 								"destinationPort": 0,
# 								"destinationPortTo": 65535,
# 								"direction": "INBOUND",
# 								"action": "DENY"
# 							}
# 						],
# 						"defaultOutboundRules": [
# 							{
# 								"sourceApplicationSecurityGroups": None,
# 								"destinationApplicationSecurityGroups": None,
# 								"name": "AllowVnetOutBound",
# 								"number": 65000,
# 								"protocol": "All",
# 								"source": "10.0.0.0/16",
# 								"destination": "10.0.0.0/16",
# 								"destinationPort": 0,
# 								"destinationPortTo": 65535,
# 								"direction": "OUTBOUND",
# 								"action": "ALLOW"
# 							},
# 							{
# 								"sourceApplicationSecurityGroups": None,
# 								"destinationApplicationSecurityGroups": None,
# 								"name": "AllowInternetOutBound",
# 								"number": 65001,
# 								"protocol": "All",
# 								"source": "0.0.0.0/0",
# 								"destination": "0.0.0.0/0",
# 								"destinationPort": 0,
# 								"destinationPortTo": 65535,
# 								"direction": "OUTBOUND",
# 								"action": "ALLOW"
# 							},
# 							{
# 								"sourceApplicationSecurityGroups": None,
# 								"destinationApplicationSecurityGroups": None,
# 								"name": "DenyAllOutBound",
# 								"number": 65500,
# 								"protocol": "All",
# 								"source": "0.0.0.0/0",
# 								"destination": "0.0.0.0/0",
# 								"destinationPort": 0,
# 								"destinationPortTo": 65535,
# 								"direction": "OUTBOUND",
# 								"action": "DENY"
# 							}
# 						],
# 						"resourceGroup": {
# 							"locks": None,
# 							"id": "/subscriptions/e584d070-3c5a-4a7c-8cf9-c063c5c67ee3/resourceGroups/rg-nsg",
# 							"type": "ResourceGroup",
# 							"name": "rg-nsg",
# 							"dome9Id": "7|0bd33263-9978-45fb-b2b8-3df69b721a3e|resourcegroup|rg-nsg",
# 							"accountNumber": "e584d070-3c5a-4a7c-8cf9-c063c5c67ee3",
# 							"region": "northeurope",
# 							"source": "db",
# 							"tags": [],
# 							"externalFindings": None
# 						},
# 						"etag": "W/\"9af9d350-d079-40cb-87e8-a27066749a47\"",
# 						"networkAssetsStats": [],
# 						"locks": None,
# 						"id": "/subscriptions/e584d070-3c5a-4a7c-8cf9-c063c5c67ee3/resourcegroups/rg-nsg/providers/microsoft.network/networksecuritygroups/anyany",
# 						"type": "NetworkSecurityGroup",
# 						"name": "anyany",
# 						"dome9Id": "7|0bd33263-9978-45fb-b2b8-3df69b721a3e|resourcegroup|rg-nsg|securitygroup|anyany",
# 						"accountNumber": "e584d070-3c5a-4a7c-8cf9-c063c5c67ee3",
# 						"region": "northeurope",
# 						"source": "db",
# 						"tags": [],
# 						"externalFindings": None
# 					},
# 					"locks": None,
# 					"type": "Subnet",
# 					"accountNumber": "e584d070-3c5a-4a7c-8cf9-c063c5c67ee3",
# 					"region": "northeurope",
# 					"source": "db",
# 					"externalFindings": None,
# 					"name": "External",
# 					"addressRange": "10.0.2.0/24",
# 					"virtualNetwork": "vnet-cplab",
# 					"tags": [],
# 					"resourceGroup": {
# 						"locks": None,
# 						"id": "/subscriptions/e584d070-3c5a-4a7c-8cf9-c063c5c67ee3/resourceGroups/rg-networking",
# 						"type": "ResourceGroup",
# 						"name": "rg-networking",
# 						"dome9Id": "7|0bd33263-9978-45fb-b2b8-3df69b721a3e|resourcegroup|rg-networking",
# 						"accountNumber": "e584d070-3c5a-4a7c-8cf9-c063c5c67ee3",
# 						"region": "northeurope",
# 						"source": "db",
# 						"tags": [],
# 						"externalFindings": None
# 					},
# 					"dome9Id": "7|0bd33263-9978-45fb-b2b8-3df69b721a3e|resourcegroup|rg-networking|virtualnetwork|vnet-cplab|subnet|external",
# 					"id": "/subscriptions/e584d070-3c5a-4a7c-8cf9-c063c5c67ee3/resourceGroups/rg-networking/providers/Microsoft.Network/virtualNetworks/vnet-cplab/subnets/External"
# 				}
# 			}
# 		],
# 		"isPublic": "true",
# 		"virtualNetwork": "vnet-cplab",
# 		"isRunning": """""false""""",
# 		"hasAgent": """""false""""",
# 		"disks": [
# 			{
# 				"name": "jenkins_OsDisk_1_997d1e36add141eeaf38e435e00092f5",
# 				"encrypted": """""false"""""
# 			}
# 		],
# 		"vmid": "ff1e23ec-faf4-4c9a-8ffd-9f8d78d0ce99",
# 		"id": "/subscriptions/e584d070-3c5a-4a7c-8cf9-c063c5c67ee3/resourcegroups/rg-jenkins/providers/microsoft.compute/virtualmachines/jenkins",
# 		"type": "VirtualMachine",
# 		"name": "jenkins",
# 		"dome9Id": "7|0bd33263-9978-45fb-b2b8-3df69b721a3e|resourcegroup|rg-jenkins|virtualmachine|jenkins",
# 		"accountNumber": "e584d070-3c5a-4a7c-8cf9-c063c5c67ee3",
# 		"region": "northeurope",
# 		"source": "0",
# 		"tags": []
# 	},
# 	"remediationActions": []
# }


ruleset_name = payload.get('bundle', {}).get('name')
ruleset_description = payload.get('bundle', {}).get('description')
ruleset_account = payload.get('account', {}).get('name')
ruleset_platform = payload.get('account', {}).get('vendor')
rule_name = payload.get('rule', {}).get('name')
rule_description = payload.get('rule', {}).get('description')
rule_severity = payload.get('rule', {}).get('severity')
finding_id = payload.get('findingKey')
finding_timestamp = payload.get('reportTime')
    # print(f'Ruleset name: {ruleset_name}')
    # print(f'Ruleset description: {ruleset_description}')
    # print(f'Cloud account: {ruleset_account}')
    # print(f'Cloud platform: {ruleset_platform}')
#review_findings_url = "https://secure.dome9.com/v2/alerts/findings?query=%7B%22sorting%22:%7B%22fieldName%22:%22createdTime%22,%22direction%22:-1%7D,%22filter%22:%7B%22fields%22:%5B%7B%22name%22:%22organizationalUnitId%22,%22value%22:%2200000000-0000-0000-0000-000000000000%22%7D%5D,%22freeTextPhrase%22:%22%" + finding_id + "%22%7D%7D"
review_findings_url = "https://secure.dome9.com/v2/alerts/findings"

teams_message = pymsteams.connectorcard('https://outlook.office.com/webhook/bcc36144-0974-4e9a-a0a0-37a6cf3654d8@612a5289-89a8-45c2-a40d-f36fadb6d37c/IncomingWebhook/d4e60fa7af07442ba0af03b889626b54/3e03697c-a186-4f64-a515-61561f591320')
teams_message.text("CloudGuard has detected a new finding")
teams_message.title("CloudGuard - Alert Notification")    
teams_message.addLinkButton("Review latest alerts", review_findings_url)
teams_message.color("ff7474")
teams_message_section = pymsteams.cardsection()
teams_message_section.activityImage("https://beckettdiags.blob.core.windows.net/web/circle-cropped.png")
teams_message_section.title("Alert Information")
teams_message_section.addFact("Ruleset Name: ", ruleset_name)
teams_message_section.addFact("Ruleset Description: ", ruleset_description)
teams_message_section.addFact("Cloud Platform / account: ", ruleset_platform + " - " + ruleset_account)
teams_message_section.addFact("Rule Name: ", rule_name)
teams_message_section.addFact("Rule Name: ", rule_description)
teams_message_section.addFact("Rule Severity: ", rule_severity)
teams_message_section.addFact("Finding ID / date: ", finding_id + " - " + finding_timestamp)
teams_message.addSection(teams_message_section)
teams_message.send()
