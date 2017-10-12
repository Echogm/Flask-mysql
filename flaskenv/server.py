from flask import Flask, render_template, redirect, session, request, flash

app = Flask(__name__)

app.secret_key = "could this be any more secret?"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/survey", methods=["POST"])
def survey():
    errors = []

    if request.form["name"] < 2:
        errors.append("Name must be 2 characters of more")

    if not request.form["name"].isalpha():
        errors.append("Name must only contain letters and not numbers")

    if len(request.form["comment"])<10:
        errors.append("Comment must be 10 characters or more")

    print errors
    session["results"] = request.form
    if len(errors) > 0:
        for error in errors:
            flash (error)
        return redirect("/")
    else:
        return redirect("/results")

@app.route("/results")
def results():
    return render_template("results.html")

app.run(debug=True)
