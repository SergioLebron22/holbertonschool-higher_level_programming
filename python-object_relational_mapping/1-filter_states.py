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
                        password='password', db=sys.argv[3])
    cur = db.cursor()

    cur.execute("""SELECT id, name FROM states ORDER BY states.id ASC""")
    rows = cur.fetchall()
    for row in rows:
        if 'N' in row[1]:
            print(row)

    cur.close()
    db.close()
