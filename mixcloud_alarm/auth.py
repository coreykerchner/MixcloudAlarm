import requests
from flask import Flask, request, redirect
from threading import Timer
import webbrowser
from mixcloud_alarm.config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

app = Flask(__name__)
access_token = None


@app.route('/')
def home():
    return redirect(f'https://www.mixcloud.com/oauth/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}')


def get_access_token(auth_code):
    url = 'https://www.mixcloud.com/oauth/access_token'
    params = {
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'client_secret': CLIENT_SECRET,
        'code': auth_code
    }
    response = requests.post(url, data=params)
    response_data = response.json()
    return response_data.get('access_token')


@app.route('/callback')
def callback():
    global access_token
    code = request.args.get('code')
    if code:
        access_token = get_access_token(code)
        print(access_token)
        print('...closing')
        return 'Authorization successful. You can close this window.'
    return 'Authorization failed.'


def run_flask():
    Timer(1, webbrowser.open(f'http://localhost:8000/')).start()
    app.run(port=8000)
