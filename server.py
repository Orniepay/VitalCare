from flask import Flask, redirect, url_for, make_response # type: ignore
from flask import render_template  # type: ignore
from flask import request # type : ignore
from flask_bcrypt import Bcrypt # type: ignore
from pymongo import MongoClient # type: ignore
import secrets
import hashlib

mongo_client = MongoClient("mongo")
db = mongo_client["cse312"]
users_collection = db["users"]

app = Flask(__name__)
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("html/index.html", title = "Home")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        password = request.form["password"]
        confirm_password = request.form['confirm_password']
        if password != confirm_password:
            return render_template("html/register.html",error=True)
        hash_password = bcrypt.generate_password_hash(password).decode()
        user = {'name': first_name + ' ' + last_name, 'password': hash_password}
        users_collection.insert_one(user)
        return redirect(url_for('login'))
    return render_template("html/register.html", title = "Register") 

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        password = request.form["password"]
        user = users_collection.find_one({'name': first_name + ' ' + last_name})
        if user:
            stored_hashed_password = user["password"]
            if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password):
                response = make_response(redirect(url_for('index')))
                token = secrets.token_hex(20)
                hashed_token = hashlib.sha256(token.encode()).hexdigest()
                users_collection.update_one({'name': first_name + ' ' + last_name }, {"$set": {"auth_token": hashed_token}})
                response.set_cookie("auth_token", token, max_age=3600, httponly=True)
                return response
    return render_template("html/login.html", title = "Login") 

@app.route('/logout')
def logout():
    auth_token = request.cookies.get('auth_token')
    if auth_token:
        users_collection.update_one({"auth_token": auth_token}, {"$unset": "auth_token"})
    response = make_response(redirect(url_for('index')))
    response.set_cookie('auth_token', '', expires=0)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)