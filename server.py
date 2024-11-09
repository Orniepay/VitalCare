from flask import Flask, render_template, request, url_for, session  # type: ignore
from pymongo import MongoClient # type: ignore

mongo_client = MongoClient("mongo")
db = mongo_client["HealthRecords"]
chat_collection = db["chat"]
users_collection = db["users"]

app = Flask(__name__)

@app.route('/')
def home_page():
    if request.method == 'GET':
        return render_template('index.html')
    #yolo
   


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

