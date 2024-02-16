#!/usr/bin/python3
"""
Module to list all states
"""
import sys
import MySQLdb


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
        print(state)

    cursor.close()
    db.close()


if __name__ == '__main__':
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    select_states(username, password, database)
