#!/usr/bin/python3
"""
this module takes a URL and an email address, sends a POST request to the
passed URL with the email as a parameter, and finally displays the body
of the response.
"""
import requests
import sys


if __name__ == "__main__":
    # get arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # prepare the data dictionary
    payload = {'email': email}

    # send the POST request
    # requests automatically encodes the dictionary into form-data
    response = requests.post(url, data=payload)

    # 4. Display the Response Body
    print(response.text)
