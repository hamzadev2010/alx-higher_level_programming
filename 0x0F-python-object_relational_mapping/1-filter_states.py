#!/usr/bin/python3
"""states with a name starting with N (upper N) from the database """
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
     cr = db.cursor()
     cr.execute("SELECT * FROM states\
                    WHERE name LIKE BINARY 'N%'\
                    ORDER BY id ASC")

    states = cr.fetchall()

    for states in states:
        print(states)
