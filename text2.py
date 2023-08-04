import sqlite3,re





get_username = input("帳號:")
sqluser1 = dict(((sqlite3.connect('static/Data/username.db')).cursor()).execute(f"SELECT * FROM 'user' WHERE username = '{get_username}'").fetchall())


get_password = input("密碼:")
sqlpassword = dict(((sqlite3.connect('static/Data/password.db')).cursor()).execute(f"SELECT * FROM 'password' WHERE password = '{get_password}'").fetchall())

if sqluser1.keys() == sqlpassword.keys():
    print("登入成功")





