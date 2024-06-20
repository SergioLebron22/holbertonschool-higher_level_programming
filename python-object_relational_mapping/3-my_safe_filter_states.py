#!/usr/bin/python3

"""
This script connects to a MySQL database and retrieves
the states that match a given name.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("""SELECT id, name FROM states WHERE name = %s
                ORDER BY states.id ASC """, (sys.argv[4],))

    rows = cur.fetchall()
    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)

    cur.close()
    db.close()
