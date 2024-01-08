#!/usr/bin/python3
"""script that takes in a URL,
sends a request to the URL
and displays the value of the variable
"""
if __name__ == '__main__':
    from sys import argv
    import requests
    web = argv[1]
    webrq = requests.get(web)
    hd= webrq.headers.get('X-Request-Id')
    print(hd)
