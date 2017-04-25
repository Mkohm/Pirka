import sqlite3
import os

# Connect to the database
home_dir = os.path.dirname(os.path.abspath(__file__)).replace("/database", "")
sqlite_file = home_dir + "/pirkabase.db"
connection = sqlite3.connect(database=sqlite_file, check_same_thread=False)


def get_values(statement: str):
    """
    This method allows the user to execute an SQL statement without have to get the cursor first
    :param statement: the statement to execute
    :return: the cursor with the data that was fetched
    """
    cursor = connection.cursor()
    cursor.execute(statement)
    return cursor.fetchall()



