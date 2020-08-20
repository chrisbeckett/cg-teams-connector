import requests

# Your API key
apiKey = 'b169ee6a-0674-4e1e-b643-0fafb3cf900f'

# Your API secret
apiSecret = 'trm5y6mjqcpzeohjctucn9mw'

headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.dome9.com/v2/Compliance/Finding/bundle/45772', params={
  'ruleLogicHash': 'xT+PHLa5oLfwTkO5DaAtUw',  'pageNumber': '1',  'pageSize': '1'
}, headers = headers, auth=(apiKey, apiSecret))

print(r.json())