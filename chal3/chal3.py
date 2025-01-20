import os
from flask import Flask, render_template, request
from datetime import datetime
from pymongo import MongoClient

# Use the MONGO_URI from the environment variable
mongo_uri = os.getenv("MONGO_URI", "mongodb://root:example@localhost:27017/")
client = MongoClient(mongo_uri)
db = client['flask_db']
records = db['records']

app = Flask(__name__)

@app.route("/")
def hello_world():
    date = datetime.now()
    client_ip = request.remote_addr
    record = {
        "ip": client_ip,
        "date": date.strftime("%Y-%m-%d %H:%M:%S")
    }
    records.insert_one(record)
    last_records = list(records.find().sort("_id", -1).limit(10))
    return render_template(
        'index.html',
        date_now=date.strftime("%d/%m/%y"),
        serveur=request.base_url,
        records=last_records
    )


@app.route("/health")
def health():
    try:
        # Check MongoDB connection
        db.command("ping")
        return "OK", 200
    except Exception as e:
        return f"Database error: {e}", 500