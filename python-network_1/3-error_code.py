#!/usr/bin/python3
"""
This script sends a request to a URL and prints the body of the response.
If an HTTP error occurs, it prints: Error code: <status code>
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode("utf-8"))

    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
