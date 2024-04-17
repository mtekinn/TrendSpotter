import os
import requests
from dotenv import load_dotenv
from reddit_api import get_access_token 
from data_utils import load_headlines, save_headlines

# Logic to ensure we have an access token (using get_access_token)
load_dotenv()
access_token = os.getenv('ACCESS_TOKEN')

if not access_token:
    access_token = get_access_token()
    if not access_token: # If we still don't have an access token, exit
        print("Exiting...")
        exit()
    else:
        print("Got a new access token!")


url = 'https://oauth.reddit.com/r/popular/hot' 
headers = {
    'User-Agent': 'MyHeadlineGeneratorApp/0.1',
    'Authorization': f'bearer {access_token}'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    new_headlines = []  

    for post in data['data']['children']:
        title = post['data']['title']
        title = title.replace('&amp;', '&').replace('&nbsp;', ' ')
        new_headlines.append(title)

    save_headlines(new_headlines)
else:
    print("Error fetching data:", response.status_code)
