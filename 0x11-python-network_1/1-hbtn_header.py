#!/usr/bin/python3
"""script that takes in a URL,
sends a request to the URL and displays the value of the X-Request-Id
"""
from sys import argv
import urllib.request


if __name__ == "__main__":
    url = argv[1]

    web = urllib.request.Request(url)
    with urllib.request.urlopen(web) as response:
        print(dict(response.headers).get("X-Request-Id"))
