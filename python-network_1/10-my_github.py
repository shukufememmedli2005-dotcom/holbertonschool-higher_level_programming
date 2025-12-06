#!/usr/bin/python3
import requests
import sys

username = sys.argv[1]
token = sys.argv[2]  # This is your personal access token, not your real password

url = "https://api.github.com/user"
response = requests.get(url, auth=(username, token))

if response.status_code == 200:
    print(response.json().get('id'))
else:
    print(None)
