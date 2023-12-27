#!/usr/bin/python3
"""lists all states from the database"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)

    cr = db.cursor()
    cr.execute("SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON cities.state_id = states.id \
    WHERE states.name = '{}';".format(argv[4]))
    st = cr.fetchall()

     print(", ".join([states[1] for states in st]))
