#!/usr/bin/python3
""" Script that f evaluates candidates applying for a back-end position
by taking 2 arg repository name and owner name
"""
from sys import argv
import requests


if __name__ == "__main__":
  web = "https://api.github.com/repos/{}/{}/commits".format(
        argv[2], argv[1])

    req = requests.get(web)
    commits = req.json()
  for i, commit in enumerate(commits[:10]):
        sha = commit.get("sha")
        author_name = commit.get("commit").get("author").get("name")
        print("{}: {}".format(sha, author_name))
