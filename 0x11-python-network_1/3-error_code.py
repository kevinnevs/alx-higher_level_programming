#!/usr/bin/python3
"""
Takes in URL, sends request to URL and displays the body of the response
print error code from 'urllib.error.HTTPError' exceptions
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            response_text = response.read().decode('utf-8')
            print(response_text)
    except urllib.error.HTTPError as error:
        print(f'Error code: {error.code}')
