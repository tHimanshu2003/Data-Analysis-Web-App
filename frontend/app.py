import os
import datetime
from flask import Flask, render_template, request
from deta import Deta
from dotenv import load_dotenv

load_dotenv()

DETA_KEY = os.environ.get("DETA_KEY")

deta = Deta(DETA_KEY)

db1 = deta.Base("Feedback")
db2 = deta.Base("Users")


def fetch_users():
    users = db2.fetch()
    return users.items


usernames = []

users = fetch_users()

for user in users:
    usernames.append(user["username"])

app = Flask(__name__)


@app.route("/")
def App():
    return render_template("app.html")


@app.route("/documentation")
def Documentation():
    return render_template("documentation.html")


@app.route("/feedback", methods=["POST", "GET"])
def Feedback():
    if request.method == "POST":
        username = request.form.get("username")
        remark = request.form.get("remark")
        date_joined = str(datetime.datetime.now())
        if username in usernames:
            db1.put({"key": username, "date_joined": date_joined, "remark": remark})
        else:
            return "Invalid Username"

    return render_template("feedback.html")


if __name__ == "__main__":
    app.run()
