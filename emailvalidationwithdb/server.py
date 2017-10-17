from flask import Flask, session, render_template, redirect, request, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "this is super secret"

db = MySQLConnector(app, "emailvalidation")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=["POST"])
def create():
    querycheck = db.query("SELECT * FROM emails;")
    for i in querycheck:
        if request.form["email"] == i["email"]:

            print "Already have that enmail"
            # flash("That email address is taken")
            return redirect("/")

    query = "INSERT INTO emails(email, createdAt, updatedAt) VALUES (:email, NOW(), NOW());"

    data = {
        "email":request.form["email"]
            }
    db.query(query,data)
    return redirect("/success")


@app.route("/success")
def success():
    emails = db.query("SELECT * FROM emails;")

    return render_template("success.html", emails=emails)

app.run(debug=True)
