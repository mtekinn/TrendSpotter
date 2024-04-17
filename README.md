# TrendSpotter

A Reddit headline collection project for generating catchy AI headlines.

## Key Features
* Fetches headlines from popular subreddits
* Stores headlines to build a unique dataset
* Secure access token handling for the Reddit API

## How to Run

**Prerequisites**
* Python 3.x 
* `requests` and `python-dotenv` libraries (install with `pip install requests python-dotenv`)

**Steps**
1. **Create a `.env` file with the following:**

CLIENT_ID=your_reddit_client_id
CLIENT_SECRET=your_reddit_client_secret

2. **Run:** `python main.py`

## Future Plans
* Implement expiration checks for access tokens
* Add more sophisticated headline cleaning
* Explore basic model training for headline generation

## Contributing
[Add guidelines for how you'd like others to contribute to your project] 