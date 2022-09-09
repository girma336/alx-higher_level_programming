#!/usr/bin/python3
"""list all states from the database"""

import MySQLdb
import sys

if __name__ = "__main__":
    db=MySQLdb.connect(host="localhost", user=argv[1],
                       port=3306, passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    for data in cur.fetchall():
        print(data)
    cur.close()
    db.close()
