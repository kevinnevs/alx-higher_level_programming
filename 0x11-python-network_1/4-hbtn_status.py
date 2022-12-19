#!/usr/bin/python3
"""
script that fetches 'https://alx-intranet.hbtn.io/status'
using the package requests
"""
import requests

response = requests.get('https://alx-intranet.hbtn.io/status')

body = response.text

print(f'Body response:\n\t- type: {type(body)}\n\t- content: {body}')
