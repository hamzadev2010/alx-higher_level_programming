#!/usr/bin/python3
"""Script that check the api with username and password
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    web = "https://api.github.com/user"
    user = argv[1]
    pswd = argv[2]
    res = requests.get(web, auth=HTTPBasicAuth(user, pswd))
    js = res.json()
    print(js.get("id"))
