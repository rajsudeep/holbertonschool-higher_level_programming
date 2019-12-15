#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """displays all values in states table where name matches the argument"""
    input_state = argv[4]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        db=argv[3])
    c = db.cursor()
    c.execute(
        "SELECT ID, name FROM states WHERE name LIKE BINARY '{}'"
        .format(input_state))
    table = c.fetchall()
    for row in table:
        print(row)
    c.close()
    db.close()
