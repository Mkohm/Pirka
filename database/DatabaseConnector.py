import sqlite3


# Connect to the database
sqlite_file = "/Users/marileonhardsen/PycharmProjects/Pirka/pirkabase.db"
connection = sqlite3.connect(sqlite_file)

def testConnection():
    cur = connection.cursor()
    cur.execute("SELECT teaching_form FROM subject")
    rows = cur.fetchall()
    print(rows)

def get_values(statement: str):
    cur = connection.cursor()
    cur.execute(statement)
    return cur.fetchall()


def add_values(statement: str):
    print("adding values")
    cur = connection.cursor()
    cur.execute(statement)
    connection.commit()

