#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user
with a letter as the q parameter and prints the result.
"""
import sys
import requests


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}

    try:
        r = requests.post(url, data=data)
        j = r.json()

        if j:
            print("[{}] {}".format(j.get("id"), j.get("name")))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
