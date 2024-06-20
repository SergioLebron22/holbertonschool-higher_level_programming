#!/usr/bin/python3


"""
This script connects to a MySQL database and retrieves all the states
whose name contains the letter 'N'. It then prints the ID and name of
each matching state.
"""


import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("""SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC""")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
