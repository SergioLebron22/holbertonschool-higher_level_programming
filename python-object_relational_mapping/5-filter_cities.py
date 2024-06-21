#!/usr/bin/python3

"""
This script retrieves cities from a MySQL database
based on a given state name.
"""


import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("""SELECT cities.id, cities.name, states.name
                 FROM cities INNER JOIN states
                 ON states.id = state_id
                 WHERE states.name = %s
                 ORDER BY cities.id ASC""", (sys.argv[4],))

    rows = cur.fetchall()

    cities = [row[1] for row in rows if row[2] == sys.argv[4]]
    print(", ".join(cities))

    cur.close()
    db.close()
