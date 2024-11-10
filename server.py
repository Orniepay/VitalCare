from flask import Flask, redirect, url_for, make_response # type: ignore
from flask import render_template  # type: ignore
from flask import request # type : ignore
from flask_bcrypt import Bcrypt # type: ignore
from pymongo import MongoClient # type: ignore
import secrets
import hashlib

mongo_client = MongoClient("mongo")
db = mongo_client["vitals_care"]
users_collection = db["users"]

app = Flask(__name__)
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    name = None
    loggedIn = False
    auth_token = request.cookies.get('auth_token')
    if auth_token:
        hasher = hashlib.sha256()
        hasher.update(auth_token.encode())
        token_hash = hasher.hexdigest()
        token_entry = users_collection.find_one({"auth_token": token_hash})
        if token_entry:
            name = token_entry["name"]
            loggedIn = True
    return render_template("html/index.html", title = "Home", name = name, loggedIn = loggedIn)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        date_of_birth = request.form["dob"]
        password = request.form["password"]
        confirm_password = request.form['confirm_password']
        existing_user = users_collection.find_one({'email': email})
        if existing_user:
            return render_template("html/register.html", exists=True)
        if password != confirm_password:
            return render_template("html/register.html",error=True)
        hash_password = bcrypt.generate_password_hash(password).decode()
        user = {'name': first_name + ' ' + last_name, 'email': email, 'date_of_birth': date_of_birth, 'password': hash_password}
        users_collection.insert_one(user)
        return redirect(url_for('login'))
    return render_template("html/register.html", title = "Register") 

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]
        user = users_collection.find_one({'email': email})
        if user:
            stored_hashed_password = user["password"]
            if bcrypt.check_password_hash(stored_hashed_password, password):
                response = make_response(redirect(url_for('index')))
                token = secrets.token_hex(20)
                hashed_token = hashlib.sha256(token.encode()).hexdigest()
                users_collection.update_one({'email': email}, {"$set": {"auth_token": hashed_token}})
                response.set_cookie("auth_token", token, max_age=3600, httponly=True)
                return response
    return render_template("html/login.html", title = "Login") 

@app.route('/logout')
def logout():
    auth_token = request.cookies.get('auth_token')
    if auth_token:
        users_collection.update_one({"auth_token": auth_token}, {"$unset": {"auth_token": auth_token}})
    response = make_response(redirect(url_for('index')))
    response.set_cookie('auth_token', '', expires=0)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)