#!/usr/bin/python3
"""states with a name starting with N (upper N) from the database """
import sys
import MySQLdb

if __name__ == '__main__':
    cn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
     cr = conn.cursor()
     cr.execute("SELECT * FROM states\
                    WHERE name LIKE BINARY 'N%'\
                    ORDER BY id ASC")

    states = cur.fetchall()

    for state in states:
        print(states)
