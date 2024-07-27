import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('MIXCLOUD_CLIENT_ID')
CLIENT_SECRET = os.getenv('MIXCLOUD_CLIENT_SECRET')
REDIRECT_URI = 'http://localhost:8000/callback'
