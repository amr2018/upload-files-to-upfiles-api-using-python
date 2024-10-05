
from dotenv import load_dotenv
from os import getenv

import requests

load_dotenv()

# load token from .env file
token = getenv('token')
endpoint = 'https://api.upfiles.com/upload'

with open('test.txt', 'rb') as file:
    files = {'file': file}
    data = {'token': token}

    res = requests.post(url = endpoint, data = data, files = files)

    result = res.json()

    print(result)
