import sqlite3


# Connect to the database
sqlite_file = "/Users/marileonhardsen/PycharmProjects/Pirka/pirkabase.db"
connection = sqlite3.connect(sqlite_file)

def testConnection(self):
    cur = self.connection.cursor()
    cur.execute("SELECT * FROM user")
    rows = cur.fetchall()
    print(rows)

def get_values(statement: str):
    cur = connection.cursor()
    cur.executescript(statement)

def add_values(statement: str):
    print("adding values")
    cur = connection.cursor()
    cur.executescript(statement)
