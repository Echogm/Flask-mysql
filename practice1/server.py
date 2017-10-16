from flask import Flask, render_template, request, redirect, session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "this is super secret"

db = MySQLConnector(app,"songs_artist")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/songs/new", methods=["POST"])
def createSong():
    query = "INSERT INTO songs(name,popularity) VALUES(:name,:popularity)"
    data = {
        "name":request.form["name"],
        "popularity":request.form["popularity"]
    }
    db.query_db(query,data)
    return redirect("/")

@app.route("/artists/new",methods=["POST"])
def createArtists(arg):

    return redirect("/")


app.run(debug=True)
