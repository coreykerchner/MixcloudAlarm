import requests

BASE_URL = 'https://api.mixcloud.com'


def get_latest_upload(username, access_token=None):
    url = f'{BASE_URL}/{username}/'
    headers = {}
    if access_token:
        headers['Authorization'] = f'Bearer {access_token}'
    response = requests.get(url, headers=headers)
    data = response.json()
    return data
