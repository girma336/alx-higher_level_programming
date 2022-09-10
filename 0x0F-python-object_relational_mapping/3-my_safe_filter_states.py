#!/usr/bin/python3
"""sefe_list all element script"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s", (argv[4],))
    for data in cur.fetchall():
        print(data)
    cur.close()
    db.close()
