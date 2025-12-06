#!/usr/bin/python3
"""
This script fetches https://intranet.hbtn.io/status using requests.
It prints the response body in a specific formatted way.
"""

import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"

    r = requests.get(url)
    body = r.text

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
