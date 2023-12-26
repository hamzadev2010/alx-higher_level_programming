#!/usr/bin/python3
""" Script that print all states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cr = db.cursor()
    cr.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cr.fetchall()
    for row in query_rows:
        if row[1].startswith("N"):
            print(row)
    cr.close()
    db.close()
    
