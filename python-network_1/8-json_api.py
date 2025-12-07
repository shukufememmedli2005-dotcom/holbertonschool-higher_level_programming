#!/usr/bin/python3
"""
this module takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    # handle the input
    # if no argument is provided, q is empty string
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    payload = {'q': letter}
    url = "http://0.0.0.0:5000/search_user"

    # send the request
    response = requests.post(url, data=payload)

    # parse the JSON
    try:
        json_response = response.json()

        # check content
        if json_response:
            # if dictionary is not empty (truthiness check)
            print("[{}] {}".format(json_response.get('id'),
                                   json_response.get('name')))
        else:
            # dictionary is empty {}
            print("No result")

    except ValueError:
        # this catches JSONDecodeError if the response isn't valid JSON
        print("Not a valid JSON")
