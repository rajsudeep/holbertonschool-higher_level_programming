#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """lists all states from the database hbtn_0e_usa"""
    db = MySQLdb.connect(
        host = "localhost",
        port = 3306,
        user = argv[1],
        password = argv[2],
        db = argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    table = c.fetchall()
    for row in table:
        print(row)
    c.close()
    db.close()
