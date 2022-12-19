#!/usr/bin/python3
"""
script that takes in URL, sends the request to URL
and displays the body of the response. If the HTTP status
code is greater than or equal to 400, print error code
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        print('Error code:', response.status_code)

    else:
        print(response.text)
