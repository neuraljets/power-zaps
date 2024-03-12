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

def get_accounts(limit=100, offset=0):
    url = f"https://server.smartlead.ai/api/v1/email-accounts"
    params = { "api_key": api_key, "limit": limit, "offset": offset }
    headers = {"accept": "application/json"}

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return None, e

    return response.json(), None

def get_all_accounts():
  limit = 100
  offset = 0
  all_accounts = []

  while True:
    accounts, error = get_accounts(limit, offset)

    if error:
      print(f"Error fetching accounts: {error}")
      return

    all_accounts.extend(accounts)

    if len(accounts) < limit:
      break

    offset += limit

  return all_accounts

store = get_store_client()
api_key = get_smartlead_api_key(store)
all_accounts = get_all_accounts()

selected_accounts = []

for account in all_accounts:
  if 'warmup_details' in account and account['warmup_details']['status'] == 'INACTIVE':
    selected_accounts.append(account)

ids = [account['id'] for account in selected_accounts]

output['ids'] = ids