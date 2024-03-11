## POWER ZAPS by NeuralJets
#
# This script will check if a Smartlead campaign needs more leads.
#
# Author:           Lauri Jutila (@ljuti)
# URL:              https://neuraljets.com
# Repository URL:   https://github.com/neuraljets/power-zaps
# License:          MIT

import requests

""" Set your Storage by Zapier key here, so that the code can access the store. """
STORE_KEY = "<set_your_store_key>"

""" Threshold is the percentage of leads that have not started yet. """
THRESHOLD = 0.2

""" Get campaign ID and prepare the output. """
campaign_id = inputData['campaign_id']
output = { "replenish": False, "campaignId": campaign_id }

def get_store_client():
    store = StoreClient(STORE_KEY)
    return store

def get_smartlead_api_key(store):
    return store.get("smartlead_api_key")

def get_campaign_status(api_key, campaign_id):
    url = f"https://server.smartlead.ai/api/v1/campaigns/{campaign_id}/analytics"
    params = { "api_key": api_key }
    headers = {"accept": "application/json"}

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return None, e

    return response.json(), None

def check_campaign_status(data):
    total_leads = data["campaign_lead_stats"]["total"]
    not_started = data["campaign_lead_stats"]["notStarted"]
    
    if not_started < total_leads * THRESHOLD:
        trigger_task()

def trigger_task():
    output["replenish"] = True

store = get_store_client()
api_key = get_smartlead_api_key(store)
data, error = get_campaign_status(api_key, campaign_id)

if error:
    print(f"Error fetching campaign status: {error}")
    return

check_campaign_status(data.json())
return output