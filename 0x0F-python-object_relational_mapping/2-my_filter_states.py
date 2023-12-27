#!/usr/bin/python3
"""Displays all values in the states table"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)

    cr = db.cursor()
    cr.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC;")
    qr = query.format(argv[4])
    cr.execute(qr)
    st = cr.fetchall()

    for states in st:
        print(states)
