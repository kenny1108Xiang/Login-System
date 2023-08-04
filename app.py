from flask import Flask, render_template, request, jsonify
# import hashlib
import sqlite3
try:    


    app = Flask(__name__, static_url_path='/static')


    # has_user = hashlib.md5(valid_credentials['user1'].encode("utf-8")).hexdigest()
    # has_pass = hashlib.md5(valid_credentials['user2'].encode("utf-8")).hexdigest()

    @app.route('/', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            sqlusername = dict(((sqlite3.connect('static/Data/username.db')).cursor()).execute(f"SELECT * FROM 'user' WHERE username = '{username}'").fetchall())
            sqlpassword = dict(((sqlite3.connect('static/Data/password.db')).cursor()).execute(f"SELECT * FROM 'password' WHERE password = '{password}'").fetchall())
            if sqlusername.keys() == sqlpassword.keys():
                return render_template('success.html')  # 顯示登入成功的頁面
            else:
                return jsonify(error="帳號或密碼錯誤")
        return render_template('login.html')


    @app.route('/page1')
    def page1():
        return render_template('page1.html')


    if __name__ == '__main__':
        app.run(debug=True)
except Exception as e:
    print(e)