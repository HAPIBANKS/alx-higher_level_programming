#!/usr/bin/python3
"""script to select all staes from sql table"""


if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for state in cur.fetchall():
        print(state)
    cur.close()
    db.close()
