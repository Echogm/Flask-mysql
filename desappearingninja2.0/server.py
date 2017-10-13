from flask import Flask, render_template, redirect, session

app = Flask(__name__)

# flag = False
# def check(x):
#     if x != "blue" or "red" or "purple" or "orange" or "ninja":
#          flag = True
#     else:
#          flag = False
#     return flag

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/ninja")
def ninja():
    return render_template("ninja.html")
# @app.route("/ninja/blue")
# def blue():
#     return render_template("blue.html")
# @app.route("/ninja/orange")
# def orange():
#     return render_template("orange.html")
# @app.route("/ninja/red")
# def red():
#     return render_template("red.html")
# @app.route("/ninja/purple")
# def purple():
#     return render_template("purple.html")
@app.route("/ninja/<x>")
def check(x):
    x = str(x)

    # if x != "blue" or "red" or "purple" or "orange":
        # return redirect("/notapril")

    if x == "blue":
        return render_template("blue.html");
    elif x == 'red':
        return render_template("red.html")
    elif x == 'purple':
        print "hi"
        return render_template("purple.html")
    elif x == "orange":
        return render_template("orange.html")
    else:
        return redirect("notapril")
@app.route("/notapril")
def notapril():
    return render_template("notapril.html")


app.run(debug=True)
