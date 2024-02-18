#!/usr/bin/python3
"""
Module to list all states
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])

    cursor = db.cursor()

    query = """
    SELECT cities.name
    FROM cities
    JOIN states
        ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id
    """

    cursor.execute(query, (argv[4],))

    result = cursor.fetchall()

    cities = ', '.join(city[0] for city in result)
    print(cities)
