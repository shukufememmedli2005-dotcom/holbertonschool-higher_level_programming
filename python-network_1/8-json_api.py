#!/usr/bin/python3
import sys
import requests

if __name__ == "__main__":
    # If no argument is given, q = ""
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}

    try:
        response = requests.post(url, data=data)
        json_data = response.json()  # Might raise ValueError

        if json_data:
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
