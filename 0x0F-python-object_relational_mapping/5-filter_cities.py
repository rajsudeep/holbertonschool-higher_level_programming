#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """takes in the name of a state as an argument and lists all cities"""
    input_state = argv[4]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        db=argv[3])
    c = db.cursor()
    query = """SELECT cities.name FROM cities
             JOIN states ON cities.state_id = states.id
             WHERE states.name = %s"""
    c.execute(query, (input_state,))
    table = c.fetchall()
    print(", ".join([row[0] for row in table]))
    c.close()
    db.close()
