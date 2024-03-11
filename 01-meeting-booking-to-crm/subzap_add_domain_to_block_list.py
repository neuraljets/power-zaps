## POWER ZAPS by NeuralJets
#
# This script adds a domain to the global block list in SmartLead.
#
# Author:           Lauri Jutila (@ljuti)
# URL:              https://neuraljets.com
# Repository URL:   https://github.com/neuraljets/power-zaps
# License:          MIT

import requests

""" Set your Storage by Zapier key here, so that the code can access the store. """
STORE_KEY = "<set_your_store_key>"
store = StoreClient(STORE_KEY)
SMARTLEAD_API_KEY = store.get("smartlead_api_key")

url = f"https://server.smartlead.ai/api/v1/leads/add-domain-block-list?api_key={SMARTLEAD_API_KEY}"

payload = { "domain_block_list": [inputData['domain']] }
headers = { "accept": "application/json", "content-type": "application/json" }

response = requests.post(url, json=payload, headers=headers)
output['status'] = response.status_code