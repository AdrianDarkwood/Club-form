from flask import Flask, render_template, request
from models import SessionLocal, Registration

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Form is Live 🚀</h1><form action='/submit' method='post'><input name='name' placeholder='Name'><input name='email' placeholder='Email'><button type='submit'>Submit</button></form>"

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]

    db = SessionLocal()
    new_entry = Registration(name=name, email=email)
    db.add(new_entry)
    db.commit()
    db.close()

    return f"<h2>✅ Thanks {name}, your data has been saved!</h2>"
