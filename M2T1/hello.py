# minimal Flask app 
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
app.config["DEBUG"] = True
#Do any app specific setup here
# for instance, loading a database

comments =[]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main_page.html", comments=comments)

    comments.append(request.form["contents"])
    return redirect(url_for('index'))

@app.route("/action")
def action():
    return "Hello from the action route!"