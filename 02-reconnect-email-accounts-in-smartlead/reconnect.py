# POWER ZAPS by NeuralJets
#
# This script instructs Smartlead to reconnect all failed email accounts.
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

url = f"https://server.smartlead.ai/api/v1/email-accounts/reconnect-failed-email-accounts"

headers = {"accept": "application/json"}
params = { "api_key": SMARTLEAD_API_KEY }

response = requests.post(url, params=params, headers=headers)
output['status'] = response.status_code