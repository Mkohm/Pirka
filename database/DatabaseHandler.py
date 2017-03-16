import sqlite3


class DatabaseHandler:

    def __init__(self):

        # Connect to the database
        self.sqlite_file = "/Users/mariuskohmann/PycharmProjects/Pirka/pirka.sqlt"
        self.connection = sqlite3.connect(self.sqlite_file)



    def testConnection(self):
        cur = self.connection.cursor()
        cur.execute("SELECT * FROM user")
        rows = cur.fetchall()
        print(rows)