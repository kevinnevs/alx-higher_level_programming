#!/usr/bin/python3
"""
takes in URL and an email, sends POST request to the passed email
displays the body of the response (decoded in UTF-8)
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data) as response:
        response_text = response.read().decode('utf-8')
        print(response_text)
