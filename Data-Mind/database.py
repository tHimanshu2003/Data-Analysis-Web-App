import os
from deta import Deta
from dotenv import load_dotenv

load_dotenv()

DETA_KEY = os.environ.get("DETA_KEY")

deta = Deta(DETA_KEY)

db = deta.Base("Users")


def insert_user(username, email, password):
    return db.put({"key": username, "email": email, "password": password})


# insert_user("peter", "google@gmail.com", "peter123")


def fetch_all_users():
    res = db.fetch()
    return res.items


# print(fetch_all_users())


def get_user(username):
    return db.get(username)


# print(get_user("peter"))


def update_user(username, updates):
    return db.update(updates, username)


# update_user("peter", updates={"email": "peter@gmail.com"})


def delete_user(username):
    return db.delete(username)


# delete_user("peter")
