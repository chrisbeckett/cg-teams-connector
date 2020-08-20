import requests

# Your API key
apiKey = 'b169ee6a-0674-4e1e-b643-0fafb3cf900f'

# Your API secret
apiSecret = 'trm5y6mjqcpzeohjctucn9mw'

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

parameters = {
  "acknowledged": True,
  "comment": "Acknowledged via Microsoft Teams"
}

finding_id = 'FJC/s9n8/Ld3yPhF9BLrSQ'
r = requests.put('https://api.dome9.com/v2/Compliance/Finding/' + finding_id + '/acknowledge', params=parameters, headers = headers, auth=(apiKey, apiSecret))

print(r)
#print(r.json())