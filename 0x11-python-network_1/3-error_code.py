#!/usr/bin/python3
"""Script that takes in a URL, sends a request
to the URL and displays the body of the response
"""
if __name__ == "__main__":
    import urllib.request
    import urllib.error
    from sys import argv
    web = argv[1]
    try:
        with urllib.request.urlopen(web) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as er:
        print("Error code: {}".format(er.code))
