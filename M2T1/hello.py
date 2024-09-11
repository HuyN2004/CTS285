# minimal Flask app 
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    # three quotes for multiline strings
    return """
    <h3>Hello from CTS285!!!</h3>
    <p> this is paragraph</p>
    <a href="action">Click here</a>



    """
@app.route("/action")
def action():
    return "Hello form the action route!"