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
            host='localhost', user=username, passwd=password, db=database
        )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)

    db.close()


if __name__ == '__main__':
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    select_states(username, password, database)
