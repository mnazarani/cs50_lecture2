from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    tag = "Welcome"
    return render_template("index.html", tag=tag)
    
