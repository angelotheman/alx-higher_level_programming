#!/usr/bin/python3
"""
Module to list all states
"""
import MySQLdb
from sys import argv


def select_states(username, password, database):
    """
    Function to select states and order them by id
    """

    db = MySQLdb.connect(
            user=username, passwd=password, db=database
        )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id"
    cursor.execute(query)

    result = cursor.fetchall()

    for state in result:
        print(state)

    db.close()


if __name__ == '__main__':
    username, password, database = argv[1], argv[2], argv[3]
    select_states(username, password, database)
