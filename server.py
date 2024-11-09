from flask import Flask # type: ignore
from flask import render_template  # type: ignore
from pymongo import MongoClient # type: ignore

mongo_client = MongoClient("mongo")
db = mongo_client["cse312"]
chat_collection = db["chat"]
users_collection = db["users"]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("html/index.html", title = "Home")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)