#!/usr/bin/python3
"""script that takes in a URL,
sends a request to the URL
and displays the value of the variable
"""
import requests
from sys import argv


if __name__ == '__main__':
    webrq = requests.get(argv[1])
    hd= webrq.headers.get('X-Request-Id')
    print(hd)
