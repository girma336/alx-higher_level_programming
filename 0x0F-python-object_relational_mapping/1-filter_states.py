#!/usr/bin/python3
"""list all states wtih a name string with N"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    for data in cur.fetchall():
        if data[1][0] == "N":
            print(data)
    cur.close()
    db.close()
