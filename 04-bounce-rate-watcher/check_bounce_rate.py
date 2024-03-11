## POWER ZAPS by NeuralJets
#
# This script will get the bounce rate of a Smartlead campaign and trigger
# an alert if it exceeds the threshold.
#
# Author:           Lauri Jutila (@ljuti)
# URL:              https://neuraljets.com
# Repository URL:   https://github.com/neuraljets/power-zaps
# License:          MIT

import requests

""" Set your Storage by Zapier key here, so that the code can access the store. """
STORE_KEY = "<set_your_store_key>"

""" Bounce Threshold is the level of bounces that will trigger the alert. """
BOUNCE_THRESHOLD = 0.02

""" Get campaign ID and prepare the output. """
campaign_id = inputData['campaign_id']
output = { "bounce_rate": "", "bounce_rate_threshold_exceeded": False, "campaignId": campaign_id }

def get_store_client():
    store = StoreClient(STORE_KEY)
    return store

def get_smartlead_api_key(store):
    return store.get("smartlead_api_key")

def get_campaign_status(api_key, campaign_id):
    url = f"https://server.smartlead.ai/api/v1/campaigns/{campaign_id}/analytics"
    headers = {"accept": "application/json"}
    params = { "api_key": api_key }

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return None, e

    return response.json(), None

def check_bounce_rate(data):
    output["campaign_name"] = data["name"]
    in_progress = data["campaign_lead_stats"]["inprogress"]
    completed = data["campaign_lead_stats"]["completed"]
    total = in_progress + completed
    bounce_count = data["campaign_lead_stats"]["blocked"]
    
    if bounce_count > total * BOUNCE_THRESHOLD:
        output["bounce_rate"] = f"{(bounce_count / total) * 100:.2f}%"
        trigger_task()

def trigger_task():
    output["bounce_rate_threshold_exceeded"] = True

store = get_store_client()
api_key = get_smartlead_api_key(store)
data, error = get_campaign_status(api_key, campaign_id)

if error:
    print(f"Error fetching campaigns: {error}")
    return

check_bounce_rate(data)