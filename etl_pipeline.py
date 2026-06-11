
import sqlite3

conn = sqlite3.connect("bluestock_mf.db")

with open("sql/schema.sql", "r") as f:
    sql_script = f.read()

conn.executescript(sql_script)

print("Tables created successfully!")

conn.close()