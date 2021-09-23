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
    acronyms = list(mongo.db.acronyms.find().collation({'locale':'en'}).sort("acronym_name", 1))
    
    return render_template("index.html", acronyms=acronyms)


@app.route("/search", methods=["GET", "POST"])
def search():
    search = request.form.get("search")
    acronyms = list(mongo.db.acronyms.find({"$text": {"$search": search}}))
    return render_template("index.html", acronyms=acronyms)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        registered_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if registered_user:
            flash("This username is registered already")
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
        return redirect(url_for("myprofile", username=session["user"])) 

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
                flash("Hello, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "myprofile", username=session["user"])) 
            else:
                flash("Login details do not match")
                return redirect(url_for("login"))

        else:
            flash("Login details do not match")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/myprofile/<username>", methods=["GET", "POST"])
def myprofile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"] == "admin":
        user_entries = list(mongo.db.acronyms.find().collation({'locale':'en'}).sort("acronym_name", 1))
        return render_template(
            "myprofile.html", username=username, user_entries=user_entries)

    if session["user"]:
        user_entries = list(mongo.db.acronyms.find(
            {"entered_by": session["user"]}).collation({'locale':'en'}).sort("acronym_name", 1))
        return render_template(
            "myprofile.html", username=username, user_entries=user_entries)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You have logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_acronym", methods=["GET", "POST"])
def add_acronym():
    if request.method == "POST":
        new_acronym = { 
                "acronym_name": request.form.get("acronym_name"),
                "meaning": request.form.get("meaning"),
                "entered_by": session["user"]
            }
        
        mongo.db.acronyms.insert_one(new_acronym)
        flash("New acronym added")
        return redirect(url_for("myprofile", username=session["user"]))

    return render_template("add_acronym.html")

@app.route("/edit_acronym/<acronym_id>", methods=["GET", "POST"])
def edit_acronym(acronym_id):
    if request.method == "POST":
        update_acronym = {
            "acronym_name": request.form.get("acronym_name"),
            "meaning": request.form.get("meaning"),
            "entered_by": session["user"]
        }
        mongo.db.acronyms.update({"_id": ObjectId(acronym_id)}, update_acronym)
        flash("Acronym updated")
        return redirect(url_for('myprofile', username=session['user']))

    entry = mongo.db.acronyms.find_one({"_id": ObjectId(acronym_id)})

    return render_template("edit_acronym.html", entry=entry)


@app.route("/delete_acronym/<acronym_id>")
def delete_acronym(acronym_id):
    mongo.db.acronyms.remove({"_id": ObjectId(acronym_id)})
    flash("Acronym deleted")
    return redirect(url_for("myprofile", username=session["user"]))


@app.route("/confirm_delete/<acronym_id>", methods=["GET", "POST"])
def confirm_delete(acronym_id):
    entry = mongo.db.acronyms.find_one({"_id": ObjectId(acronym_id)})
    return render_template("confirm_delete.html", entry=entry)



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
