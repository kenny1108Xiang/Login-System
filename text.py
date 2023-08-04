import sqlite3
import re
sql_data = sqlite3.connect("static/Data/data.db")
cursor = sql_data.cursor()
cursor.execute("SELECT * FROM 'data'")
records = cursor.fetchall()



valid_credentials = records

print(records)

print(type(records))