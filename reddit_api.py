import requests
import os
import time
from dotenv import load_dotenv, set_key

load_dotenv()
access_token = os.getenv('ACCESS_TOKEN')
access_token_expires = int(os.getenv('ACCESS_TOKEN_EXPIRES', 0)) # Ensure a default value of 0

# get the client_id and client_secret from the .env file
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

def get_access_token():
    auth_url = 'https://www.reddit.com/api/v1/access_token'
    data = {
        'grant_type': 'client_credentials'
    }
    auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    response = requests.post(auth_url, data=data, headers={'User-Agent': 'MyHeadlineGeneratorApp/0.1'}, auth=auth)

    current_time = int(time.time())

    if not access_token or current_time >= access_token_expires:
        # get a new access token
        if response.status_code == 200:
            token_data = response.json()
            access_token = token_data['access_token']
            expires_in = token_data['expires_in']

            load_dotenv()
            set_key('.env', 'ACCESS_TOKEN', access_token)
            set_key('.env', 'ACCESS_TOKEN_EXPIRES', str(current_time + expires_in))

            return access_token
        else:
            print("Error fetching access token:", response.status_code)
            return None
    else:
        return access_token