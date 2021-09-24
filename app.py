import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

# Configuration
app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


# Get list of all acronyms, sort by name alphabetically ( no upper case priority )
@app.route("/")
@app.route("/get_acronyms")
def get_acronyms():
    acronyms = list(mongo.db.acronyms.find().collation(
        {'locale':'en'}).sort("acronym_name", 1))    
    return render_template("index.html", acronyms=acronyms)


# Search bar for main page
@app.route("/search", methods=["GET", "POST"])
def search():
    search = request.form.get("search")
    acronyms = list(mongo.db.acronyms.find({"$text": {"$search": search}}))
    return render_template("index.html", acronyms=acronyms)


# Registration 
# User Authentication example shown in MongoDB walkthrough lesson 
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        registered_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # Check if user already in database
        if registered_user:
            flash("This username already exists")
            return redirect(url_for("register"))
        # Check if passwords match    
        if request.form.get("password") != request.form.get("password-2"):
            flash("Passwords do not match")
            return redirect(url_for("register"))
        # If passwords match, and username is not in use, insert user into database
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)
        session["user"] = request.form.get("username").lower()
        flash("You have successfully reigistered")
        return redirect(url_for("myprofile", username=session["user"])) 
    return render_template("register.html") 


# Login
# User Authentication example shown in MongoDB walkthrough lesson
@app.route("/login", methods=["GET", "POST"])
def login():
    # Get username form data 
    if request.method == "POST":
        registered_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # Check if password hash matches with hash in user database
        if registered_user:
            if check_password_hash(
                registered_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Hello, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "myprofile", username=session["user"]))
            # If password hash doesn't match, redirect to login page          
            else:
                flash("Login details do not match")
                return redirect(url_for("login"))
            # if username doesn't match, redirect to login page
        else:
            flash("Login details do not match")
            return redirect(url_for("login"))
    return render_template("login.html")


# Myprofile 
@app.route("/myprofile/<username>", methods=["GET", "POST"])
def myprofile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    # User "admin" functionality, lists every user entries in profile page
    if session["user"] == "admin":
        user_entries = list(mongo.db.acronyms.find().collation(
            {'locale':'en'}).sort("acronym_name", 1))
        return render_template(
            "myprofile.html", username=username, user_entries=user_entries)
    # Registered user functionality, lists registered users entries
    if session["user"]:
        user_entries = list(mongo.db.acronyms.find(
            {"entered_by": session["user"]}).collation(
                {'locale':'en'}).sort("acronym_name", 1))
        return render_template(
            "myprofile.html", username=username, user_entries=user_entries)
    return redirect(url_for("login"))


# Logout
# User Authentication example shown in MongoDB walkthrough lesson 
@app.route("/logout")
def logout():
    # Remove user cookie from session
    flash("You have logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Add acronym
@app.route("/add_acronym", methods=["GET", "POST"])
def add_acronym():
    # Get form data
    if request.method == "POST":
        new_acronym = { 
                "acronym_name": request.form.get("acronym_name").upper(),
                "meaning": request.form.get("meaning"),
                "entered_by": session["user"]
            }
        # Check if entry name already exists in database
        entries = list(mongo.db.acronyms.find())
        for entry in entries:
            for key, value in entry.items():
                if value == request.form.get("acronym_name").upper():
                    flash("This acronym already exists")
                    return redirect(url_for("add_acronym")) 
        # If entry name is not in database, insert new entry
        mongo.db.acronyms.insert_one(new_acronym)
        flash("New acronym added")
        return redirect(url_for("myprofile", username=session["user"]))
    return render_template("add_acronym.html")


# Edit acronym
@app.route("/edit_acronym/<acronym_id>", methods=["GET", "POST"])
def edit_acronym(acronym_id):
    # Get form data
    if request.method == "POST":
        update_acronym = {
            "acronym_name": request.form.get("acronym_name"),
            "meaning": request.form.get("meaning"),
            "entered_by": session["user"]
        }
        # Update acronym
        mongo.db.acronyms.update({"_id": ObjectId(acronym_id)}, update_acronym)
        flash("Acronym updated")
        return redirect(url_for('myprofile', username=session['user']))
    # Get acronym data from database to reflect it in edit form 
    entry = mongo.db.acronyms.find_one({"_id": ObjectId(acronym_id)})
    return render_template("edit_acronym.html", entry=entry)


# Delete
@app.route("/delete_acronym/<acronym_id>")
def delete_acronym(acronym_id):
    # remove acronym from database
    mongo.db.acronyms.remove({"_id": ObjectId(acronym_id)})
    flash("Acronym deleted")
    return redirect(url_for("myprofile", username=session["user"]))


# Confirm delete message/page
@app.route("/confirm_delete/<acronym_id>", methods=["GET", "POST"])
def confirm_delete(acronym_id):
    entry = mongo.db.acronyms.find_one({"_id": ObjectId(acronym_id)})
    return render_template("confirm_delete.html", entry=entry)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
