#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response
"""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":

    web = argv[1]
    val = {'email': argv[2]}

    db = urllib.parse.urlencode(val).encode()
    rq = urllib.request.Request(web, db)
    with urllib.request.urlopen(rq) as response:
        value = response.read().decode('utf8')
    print(value)
