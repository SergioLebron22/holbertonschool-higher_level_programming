#!/usr/bin/python3

"""
This script connects to a MySQL database and
retrieves the id and name of all states
from the 'states' table.
"""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("""SELECT id, name FROM states ORDER BY states.id ASC""")
    rows = cur.fetchall()
    for row in rows:
        print(f"{row}")

    cur.close()
    db.close()
