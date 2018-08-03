import datetime

from flask import Flask, render_template, request, session
from flask_session import Session  

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False   
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    tag = "Welcome"
    return render_template("index.html", tag=tag)
    
@app.route("/newyear")
def newyear():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    return render_template("newyear.html", new_year=new_year)
    
    
@app.route("/hello", methods=['POST', 'GET'])
def hello():
    if request.method == 'GET':
        return "Please submit the form"
    else:
        name = request.form.get('name')
        return render_template("hello.html", name=name)

@app.route("/notes", methods=['POST', 'GET'])
def notes():
    if session.get("notes") is None:
        session['notes'] = []
    if request.method == "POST":   
        note = request.form.get('note')
        session['notes'].append(note)
        
    return render_template("notes.html", notes=session['notes'])
    
    

    
