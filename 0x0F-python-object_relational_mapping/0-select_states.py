#!/usr/bin/python3
"""lists all states from the database"""

import sys
import MySQLdb

if __name__ == '__main__':
    cn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cr = cn.cursor()
    cr.execute("SELECT * FROM states;")
    states = cr.fetchall()

    for state in states:
        print(states)
