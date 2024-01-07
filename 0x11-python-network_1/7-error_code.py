#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and displays the body of the response.
"""
import requests
from sys import argv

if __name__ == '__main__':

    webrq = requests.get(argv[1])

    if webrq.status_code >= 400:
        print("Error code: {}".format(webrq.status_code))
    else:
        print(webrq.text)
