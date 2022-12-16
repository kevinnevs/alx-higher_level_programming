#!/usr/bin/python3
"""
script that takes in URL, sends request
and displays the value of 'X-Request-Id variable'
"""
import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    request_id = response.getheader('X-Request-Id')

print(request_id)
