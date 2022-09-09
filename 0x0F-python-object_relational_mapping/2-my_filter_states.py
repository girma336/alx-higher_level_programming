#!/usr/bin/python3
"""list all using argument value"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], db=argv[3],
                         passwd=argv[2])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    for data in cur.fetchall():
        if data[1] == argv[4]:
            print(data)
    cur.close()
    db.close()
