#!/usr/bin/python3
"""
This script sends a POST request with an email and prints the response body.
"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # encode the POST data
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # send the request
    with urllib.request.urlopen(url, data=data) as response:
        body = response.read()
        print(body.decode('utf-8'))
