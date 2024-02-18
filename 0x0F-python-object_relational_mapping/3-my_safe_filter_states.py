#!/usr/bin/python3
"""
Module to list all states
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE BINARY name = %s"

    cursor.execute(query, (argv[4],))

    result = cursor.fetchall()

    for state in result:
        print(state)
