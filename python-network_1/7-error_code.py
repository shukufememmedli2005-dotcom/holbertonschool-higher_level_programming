#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response.
Prints "Error code: <status>" if status >= 400.
"""
import sys
import requests

url = sys.argv[1]

try:
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
except requests.RequestException as e:
    print(f"Error code: {getattr(e.response, 'status_code', 'Unknown')}")
