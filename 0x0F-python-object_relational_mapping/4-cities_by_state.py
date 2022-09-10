#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                   FROM cities INNER JOIN states
                   ON cities.state_id = states.name""")
    for data in cur.fetchall():
        print(data)
    cur.close()
    db.close()
