#!/usr/bin/python3
"""lists all cities of that state, using the database"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.name
                   FROM cities JOIN states
                   ON cities.state_id = states.id
                   WHERE states.name = %s""", (argv[4],))
    result = cur.fetchall()
    lenght = len(result)
    if lenght == 0:
        print('')
    for i in range(lenght):
        if i < lenght - 1:
            print(result[i][0], end=', ')
        else:
            print(result[i][0])
    cur.close()
    db.close()
