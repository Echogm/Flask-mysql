from flask import Flask, render_template, request, redirect, session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "this is secret"

db = MySQLConnector(app, "friends")

@app.route("/")
def index():
    friends = db.query("SELECT * FROM friends;")
    # name = request.form("name")
    # age = request.form("age")
    return render_template("index.html", friends=friends)

@app.route("/addfriend", methods=["POST"])
def create():

    query = "INSERT INTO friends(name, age, createdAt, updatedAt) VALUES (:name, :age, :NOW(), :NOW());"

    data = {
        "name":request.form["name"],
        "age":request.form["age"]
    }

    db.query(query,data)
    return redirect("/")

app.run(debug=True)
