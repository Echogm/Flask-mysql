from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/ninjas")
def ninja():
    return render_template("ninja.html")
@app.route("/dojos/new", methods=["POST"])
def dojos():
    session["results"] = request.form
    return render_template("dojos.html"), redirect("/ninjas")
app.run(debug=True)
