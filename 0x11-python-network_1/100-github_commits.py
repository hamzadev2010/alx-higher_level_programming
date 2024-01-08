#!/usr/bin/python3
""" Script that f evaluates candidates applying for a back-end position
by taking 2 arg repository name and owner name
"""
from sys import argv
import requests


if __name__ == "__main__":

  web = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
  req = requests.get(web)
  commits = req.json()
  for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
