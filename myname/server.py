from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "i am super secret"
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/process", methods=["POST"])
def process():
    names = []
    session["results"] = request.form
    names.append("names")
    return redirect("/")
app.run(debug=True)
