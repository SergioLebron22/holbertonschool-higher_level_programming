#!/usr/bin/python3

"""
This script connects to a MySQL database and retrieves data
from the 'cities' and 'states' tables.
It prints the ID, name of the city,
and name of the state for each row in the result set.
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
                 ON states.id = state_id ORDER BY cities.id ASC""")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
