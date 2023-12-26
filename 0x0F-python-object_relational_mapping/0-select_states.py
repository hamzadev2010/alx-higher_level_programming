!/usr/bin/python3
"""lists all states from the database"""

import sys
import MySQLdb

if __name__ == "__main__":
    cn = MySQLdb.connect(host='localhost', charset="utf8", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cr = cn.cursor()
    cr.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cr.fetchall()
    for row in query_rows:
        print(row)
    cr.close()
    cn.close()
