import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)

@app.route("/")
@app.route("/get_acronyms")
def get_acronyms():
    acronyms = list(mongo.db.acronyms.find())
    return render_template("index.html", acronyms=acronyms)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        registered_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if registered_user:
            flash("This username is already registered")
            return redirect(url_for("register"))
        if request.form.get("password") != request.form.get("password-2"):
            flash("Passwords do not match")
            return redirect(url_for("register"))
        
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)
        session["user"] = request.form.get("username").lower()
        flash("You have successfully reigistered")
            
    return render_template("register.html") 


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        registered_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if registered_user:
            if check_password_hash(
                registered_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Hello, {}".format(request.form.get("username")))
            else:
                flash("Login details do not match")
                return redirect(url_for("login"))

        else:
            flash("Login details do not match")
            return redirect(url_for("login"))
    return render_template("login.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
