import sqlite3

init_sql_file = "./db/init.sql"

conn = sqlite3.connect("database.db")
cursor = conn.cursor()
def init():
    with open(init_sql_file, "r") as sql_file:
        sql_script = sql_file.read()
        cursor.executescript(sql_script)



conn.commit()
conn.close()
