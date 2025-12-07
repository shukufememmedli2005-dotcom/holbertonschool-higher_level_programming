#!/usr/bin/python3
"""
this module takes a URL, sends a request to the URL and displays the
body of the response. if the HTTP status code is greater than or equal
to 400, it prints the error code instead.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    # the requests library does not raise an exception for 4xx/5xx codes
    # by default. it checks the status_code attribute manually.
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
