from datetime import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(
    "mongodb+srv://thinkingdatascience:microblog@microblog-application.u2vobau.mongodb.net/"
)

app.db = client.microblog


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        entry_content = request.form.get("content")
        formatted_date = datetime.today().strftime("%b %d")
        app.db.entries.insert_one({"content": entry_content, "date": formatted_date})

    entries = [(entry["content"], entry["date"]) for entry in app.db.entries.find({})]

    return render_template("home.html", entries=entries)
