import os
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('MIXCLOUD_CLIENT_ID')
CLIENT_SECRET = os.getenv('MIXCLOUD_CLIENT_SECRET')
REDIRECT_URI = os.getenv('MIXCLOUD_REDIRECT_URI')


def get_access_token(auth_code):
    url = 'https://www.mixcloud.com/oauth/access_token'
    params = {
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'client_secret': CLIENT_SECRET,
        'code': auth_code
    }
    response = requests.post(url, params=params)
    response_data = response.json()
    return response_data.get('access_token')


def get_authorization_url():
    return f'https://www.mixcloud.com/oauth/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}'

