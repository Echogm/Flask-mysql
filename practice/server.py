from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "i'm secret secrests"
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/ninjas")
def ninja():
    return render_template("ninja.html")
@app.route("/dojos/new")
def dojos():
    # session["results"] = request.form
    return render_template ("dojos.html")
app.run(debug=True)
