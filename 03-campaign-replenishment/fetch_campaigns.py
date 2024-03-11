## POWER ZAPS by NeuralJets
#
# This script will get active campaigns from Smartlead.
#
# Author:           Lauri Jutila (@ljuti)
# URL:              https://neuraljets.com
# Repository URL:   https://github.com/neuraljets/power-zaps
# License:          MIT

import requests

""" Set your Storage by Zapier key here, so that the code can access the store. """
STORE_KEY = "<set_your_store_key>"

def get_store_client():
    store = StoreClient(STORE_KEY)
    return store

def get_smartlead_api_key(store):
    return store.get("smartlead_api_key")

def fetch_campaigns(api_key):
    url = f"https://server.smartlead.ai/api/v1/campaigns"
    params = {"api_key": api_key}
    headers = {"accept": "application/json"}

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return None, e

    return response.json(), None

store = get_store_client()
api_key = get_smartlead_api_key(store)
data, error = fetch_campaigns(api_key)

if error:
    print(f"Error fetching campaigns: {error}")
    return

active_ids = [item['id'] for item in data if item['status'] == 'ACTIVE']
output['campaign_ids'] = active_ids
return output
