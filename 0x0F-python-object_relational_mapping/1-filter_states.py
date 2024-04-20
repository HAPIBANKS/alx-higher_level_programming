#!/usr/bin/pyhton3
"""Filter states that start with N from a database
hbtn_0e_0usa using the module MySQLdb"""


if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(user=sys.argv[1],
                         passwrd=sys.argv[2],
                         database=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    for state in cur.fetchall:
        print(state)
    cur.close()
    db.close()
