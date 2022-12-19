#!/usr/bin/python3
"""
script that takes GitHub credentials and uses the GitHub API
to display the ID. We must use PAK, not password
"""
import requests
import sys


def github_api():
    username = sys.argv[1]
    password = sys.argv[2]

    api_url = "https://api.github.com/user"

    auth = (username, password)

    response = requests.get(api_url, auth=auth)

    if response.status_code == 200:
        user_info = response.json()
        print(user_info['id'])
    else:
        print(None)


if __name__ == "__main__":
    github_api()
