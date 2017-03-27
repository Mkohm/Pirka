import sqlite3
from os.path import expanduser
import os

# Connect to the database
home_dir = os.path.dirname(os.path.abspath(__file__)).replace("/database", "")
sqlite_file = home_dir + "/pirkabase.db"
print(sqlite_file)

connection = sqlite3.connect(database=sqlite_file, check_same_thread=False)




def testConnection():
    cur = connection.cursor()
    cur.execute("SELECT teaching_form FROM subject")
    rows = cur.fetchall()
    print(rows)

def get_values(statement: str):
    cur = connection.cursor()
    cur.execute(statement)
    return cur.fetchall()



