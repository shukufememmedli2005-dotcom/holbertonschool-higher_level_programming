#!/usr/bin/python3
import sys
from urllib import request

url = sys.argv[1]

with request.urlopen(url) as response:
    print(response.headers.get("X-Request-Id"))
