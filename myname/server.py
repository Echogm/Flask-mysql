from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "i am super secret"
x = []
@app.route("/")
def index():

    return render_template("index.html", x = x)
@app.route("/process", methods=["POST"])
def process():
    # print request.form["name"]
    x.append(request.form["name"])
    return redirect("/")
app.run(debug=True)
