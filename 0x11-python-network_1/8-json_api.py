#!/usr/bin/python3
""" Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user
"""
from sys import argv
import requests


if __name__ == "__main__":
    web = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = argv[1]
    else:
        q = ""
    req = {"q": q}
    res = requests.post(web, data=req)
    try:
        json_output = res.json()
        if not json_output:
            print("No result")
        else:
            idd = json_outp.get("id")
            name = json_outp.get("name")
            print("[{}] {}".format(idd, name))
    except ValueError as invalid_json:
        print("Not a valid JSON")
