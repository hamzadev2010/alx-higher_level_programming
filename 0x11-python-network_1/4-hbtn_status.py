#!/usr/bin/python3
"""script that fetches and send response"""
if __name__ == "__main__":
    import requests
    web = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(web.text)))
    print("\t- content: {}".format(web.text))
