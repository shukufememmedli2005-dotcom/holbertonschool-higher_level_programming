#!/usr/bin/python3
"""
this module takes a URL, sends a request to the URL and displays the value
of the variable X-Request-Id in the response header.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    # send request
    response = requests.get(url)

    # access headers
    # response.headers is a dictionary-like object.
    # it uses .get() to safely retrieve the specific header.
    print(response.headers.get('X-Request-Id'))
