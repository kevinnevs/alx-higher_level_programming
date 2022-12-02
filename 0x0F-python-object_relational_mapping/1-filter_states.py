#!/usr/bin/python3
"""
Lists all States with a name starting with N from the db hbtn_0e_0_usa
"""

import MySQLdb
import sys


def get_states():
    """
    Takes arguments argv to list databases

    Arguments:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    rows = cur.fetchall()
    for i in rows:
        print(i)

    cur.close()
    db.close()


if __name__ == "__main__":
    get_states()
