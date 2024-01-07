#!/usr/bin/python3
"""script that takes your GitHub credentials
(username and password) and uses the GitHub API
"""
import requests
from sys import argv
import requests.auth


if __name__ == "__main__":

      webreq = requests.get("https://api.github.com/user", auth=auth)
       auth = requests.auth.HTTPBasicAuth(argv[1], argv[2])
       print(webreq.json().get("id"))
