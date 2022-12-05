#!/usr/bin/python3
"""
Takes an argument and displays values of State, where name matches argument
Prevents SQL Injection passed on arguments by return arguments not included
"""

import MySQLdb
import sys


def filter_names_safe():
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

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE BINARY name=%s ORDER BY states.id"
    cursor.execute(query, (sys.argv[4],))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_names_safe()
