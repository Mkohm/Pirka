import sqlite3

# Connect to the database
sqlite_file = "/Users/mariuskohmann/PycharmProjects/Pirka/pirkabase.db"
connection = sqlite3.connect(sqlite_file)

@staticmethod
def testConnection(self):
    cur = self.connection.cursor()
    cur.execute("SELECT * FROM user")
    rows = cur.fetchall()
    print(rows)


@staticmethod
def get_values(statement: str):
    cur = connection.cursor()
    cur.executescript(statement)

def add_values(statement: str):
    print("adding values")
    cur = connection.cursor()
    cur.executescript(statement)

