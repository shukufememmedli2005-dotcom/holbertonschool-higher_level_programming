#!/usr/bin/python3
"""
this module takes GitHub credentials (username and password)
and uses the GitHub API to display the user id.
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    user = sys.argv[1]
    pwd = sys.argv[2]
    response = requests.get(url, auth=(user, pwd))
    print(response.json().get('id'))
