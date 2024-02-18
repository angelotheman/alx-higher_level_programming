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

    query = "SELECT * FROM states WHERE name LIKE 'N%'"
    cursor.execute(query)

    result = cursor.fetchall()

    for state in result:
        print("({}, '{}')".format(state[0], state[1]))

    db.close()


if __name__ == '__main__':
    username, password, database = argv[1], argv[2], argv[3]
    select_states(username, password, database)
