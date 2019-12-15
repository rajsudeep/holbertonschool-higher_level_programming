#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """lists all cities from htbn_0e_4_usa"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        db=argv[3])
    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name FROM cities" +
              "LEFT JOIN states ON cities.state_id = states.id")
    table = c.fetchall()
    for row in table:
        print(row)
    c.close()
    db.close()
