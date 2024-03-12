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
STORE_KEY = "<set-the-store-key>"
store = StoreClient(STORE_KEY)
SMARTLEAD_API_KEY = store.get("smartlead_api_key")

url = f"https://server.smartlead.ai/api/v1/email-accounts"

headers = {"accept": "application/json"}
params = { "api_key": SMARTLEAD_API_KEY }

response = requests.post(url, params=params, headers=headers)

def get_store_client():
    store = StoreClient(STORE_KEY)
    return store

def get_smartlead_api_key(store):
    return store.get("smartlead_api_key")

def set_warmup_configuration(id):
    url = f"https://server.smartlead.ai/api/v1/email-accounts/{id}/warmup"
    payload = { "warmup_enabled": "true", "total_warmup_per_day": 40, "daily_rampup": 5, "reply_rate_percentage": "45" }
    params = { "api_key": api_key }
    headers = {"accept": "application/json"}

    try:
        response = requests.post(url, json=payload, params=params, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return None, e

    return response, None

account_id = inputData["id"]
store = get_store_client()
api_key = get_smartlead_api_key(store)
response = set_warmup_configuration(account_id)
output['status'] = response.status_code