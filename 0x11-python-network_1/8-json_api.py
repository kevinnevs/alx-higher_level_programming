#!/usr/bin/python3
"""
takes in a letter and sends a POST requests to
'http://0.0.0.0:5000/search_user' with the letter as a parameter
"""
import json
import requests
import sys


def search_api():
    """status"""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    response = requests.post('http://0.0.0.0:5000/search_user',
                             data={'q': q})

    try:
        data = response.json()
    except ValueError:
        print("Not a valid JSON")
        sys.exit()

    if not data:
        print("No reesult")
    else:
        print("[{}] {}".format(data['id'], data['name']))


if __name__ == "__main__":
    search_api()
