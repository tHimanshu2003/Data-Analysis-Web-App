import os
import datetime
from flask import Flask, render_template, request, flash
from deta import Deta
from dotenv import load_dotenv

load_dotenv()

DETA_KEY = os.environ.get("DETA_KEY")

deta = Deta(DETA_KEY)

db1 = deta.Base("Feedback")
db2 = deta.Base("Users")
db3 = deta.Base("Delete_Account")


def fetch_users():
    users = db2.fetch()
    return users.items


usernames = []

users = fetch_users()

for user in users:
    usernames.append(user["username"])

app = Flask(__name__)
app.secret_key = "xyz"


@app.route("/")
def App():
    return render_template("app.html")


@app.route("/delete", methods=["POST", "GET"])
def Documentation():
    if request.method == "POST":
        username = request.form.get("username")
        date = str(datetime.datetime.now())
        if username in usernames:
            db3.put({"key": username, "date": date})
            flash("Success! Your response recorded", "success")
        else:
            flash("Invalid Username", "error")
    return render_template("delete_account.html")


@app.route("/feedback", methods=["POST", "GET"])
def Feedback():
    if request.method == "POST":
        username = request.form.get("username")
        remark = request.form.get("remark")
        date = str(datetime.datetime.now())
        if username in usernames:
            db1.put({"key": username, "date": date, "remark": remark})
            flash("Success! Your response recorded", "success")
        else:
            flash("Invalid Username", "error")

    return render_template("feedback.html")


if __name__ == "__main__":
    app.run()
