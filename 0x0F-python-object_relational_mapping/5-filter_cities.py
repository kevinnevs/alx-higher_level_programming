#!/usr/bin/python3
"""
Takes in state as argument  and list all the cities of that state
In the hbtn_0e_4_usa database
"""

import MySQLdb
import sys


def filter_cities():
    """
    Takes arguments argv to list databases

    Arguments:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
        argv[4]: argument name
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    cur = db.cursor()

    state_name = sys.argv[4]

    cur.execute("SELECT cities.name FROM cities INNER JOIN states\
                ON cities.state_id = states.id WHERE states.name=%s\
                ORDER BY cities.id ASC", (state_name,))

    print(", ".join([row[0] for row in cur.fetchall()]))

    cur.close()
    db.close()


if __name__ == "__main__":
    filter_cities()
