import sqlite3
from os.path import expanduser


# Connect to the database
home_dir = expanduser("~")
sqlite_file = home_dir + "/PycharmProjects/Pirka/pirkabase.db"

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


def add_values(statement: str, data_variables):
    print("adding values")
    cur = connection.cursor()
    cur.execute(statement)
    connection.commit()
