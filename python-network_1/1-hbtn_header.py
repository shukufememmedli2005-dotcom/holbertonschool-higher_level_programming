#!/usr/bin/python3
"""
Python script that fetches the value of X-Request-Id from a URL's
response header.

Usage: ./1-hbtn_header.py <URL>
"""
import sys
from urllib import request

if len(sys.argv) < 2:
    print("Usage: ./1-hbtn_header.py <URL>")
    sys.exit(1)

url = sys.argv[1]

with request.urlopen(url) as response:
    print(response.headers.get("X-Request-Id"))
