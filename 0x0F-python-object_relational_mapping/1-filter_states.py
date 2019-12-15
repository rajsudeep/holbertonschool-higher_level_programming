#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """lists all states with a name starting with N from hbtn_0e_0_usa"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        db=argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'")
    table = c.fetchall()
    for row in table:
        print(row)
    c.close()
    db.close()
