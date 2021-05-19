from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route('/users')
def read():
    mysql = connectToMySQL("users_schema")
    users = mysql.query_db("SELECT * FROM users;")
    print(users)
    return render_template("read.html", all_users = users)

@app.route('/users/create', methods=['POST', 'GET'])
def create():
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(email)s, NOW(), NOW());"
    data = {
        'fn': request.form['fname'],
        'ln': request.form['lname'],
        'email': request.form['email'],
    }
    db = connectToMySQL('users_schema')
    db.query_db(query, data)
    return redirect('/users')

@app.route('/users/new')
def new_user():
    return render_template('create.html')

if __name__ == "__main__":
    app.run(debug=True)