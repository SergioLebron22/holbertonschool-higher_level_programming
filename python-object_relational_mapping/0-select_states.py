#!/usr/bin/python3

import MySQLdb
import sys

db = MySQLdb.connect(host='localhost', user=sys.argv[1], password='password', db=sys.argv[3])
cur = db.cursor()

cur.execute("""SELECT id, name FROM states ORDER BY states.id ASC""")
rows = cur.fetchall()
for row in rows:
    print(f"{row}")
