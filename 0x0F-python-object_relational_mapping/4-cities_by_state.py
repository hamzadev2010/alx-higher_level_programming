#!/usr/bin/python3
"""script that lists all cities from the database"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)

    cr = db.cursor()
    cr.execute("SELECT cities.id, citirs.name, states.name
          FROM states , cities 
          WHERE cities.state_id = states.id
          ORDER BY cities.id ASC")
    st = cr.fetchall()

    for states in st:
        print(states) 
