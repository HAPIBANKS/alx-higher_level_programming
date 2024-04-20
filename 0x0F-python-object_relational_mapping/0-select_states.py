#!/usr/bin/python3
import MYSQLdb
import sys


def list_states{username, password, database):

    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=database,
                         port=3308)
    cur = db.cursor()
    cur.execute("SELECT *FROM states ORDER BY id")
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)
