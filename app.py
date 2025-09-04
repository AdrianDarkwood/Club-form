from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from sqlalchemy import inspect

app = Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL").replace("postgres://", "postgresql://")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Model
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member1_name = db.Column(db.String(100), nullable=False)
    member1_email = db.Column(db.String(120), nullable=False)
    member1_branch = db.Column(db.String(50), nullable=False)
    member1_usn = db.Column(db.String(20))
    member1_phone = db.Column(db.String(15))

    member2_name = db.Column(db.String(100))
    member2_email = db.Column(db.String(120))
    member2_branch = db.Column(db.String(50))
    member2_usn = db.Column(db.String(20))
    member2_phone = db.Column(db.String(15))

    member3_name = db.Column(db.String(100))
    member3_email = db.Column(db.String(120))
    member3_branch = db.Column(db.String(50))
    member3_usn = db.Column(db.String(20))
    member3_phone = db.Column(db.String(15))

    member4_name = db.Column(db.String(100))
    member4_email = db.Column(db.String(120))
    member4_branch = db.Column(db.String(50))
    member4_usn = db.Column(db.String(20))
    member4_phone = db.Column(db.String(15))

    member5_name = db.Column(db.String(100))
    member5_email = db.Column(db.String(120))
    member5_branch = db.Column(db.String(50))
    member5_usn = db.Column(db.String(20))
    member5_phone = db.Column(db.String(15))

    member6_name = db.Column(db.String(100))
    member6_email = db.Column(db.String(120))
    member6_branch = db.Column(db.String(50))
    member6_usn = db.Column(db.String(20))
    member6_phone = db.Column(db.String(15))

    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)


# ✅ Create tables only if they don't exist
with app.app_context():
    inspector = inspect(db.engine)
    if not inspector.has_table("registration"):
        db.create_all()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    registration = Registration(
        member1_name=request.form["member1_name"],
        member1_email=request.form["member1_email"],
        member1_branch=request.form["member1_branch"],
        member1_usn=request.form.get("member1_usn"),
        member1_phone=request.form.get("member1_phone"),

        member2_name=request.form.get("member2_name"),
        member2_email=request.form.get("member2_email"),
        member2_branch=request.form.get("member2_branch"),
        member2_usn=request.form.get("member2_usn"),
        member2_phone=request.form.get("member2_phone"),

        member3_name=request.form.get("member3_name"),
        member3_email=request.form.get("member3_email"),
        member3_branch=request.form.get("member3_branch"),
        member3_usn=request.form.get("member3_usn"),
        member3_phone=request.form.get("member3_phone"),

        member4_name=request.form.get("member4_name"),
        member4_email=request.form.get("member4_email"),
        member4_branch=request.form.get("member4_branch"),
        member4_usn=request.form.get("member4_usn"),
        member4_phone=request.form.get("member4_phone"),

        member5_name=request.form.get("member5_name"),
        member5_email=request.form.get("member5_email"),
        member5_branch=request.form.get("member5_branch"),
        member5_usn=request.form.get("member5_usn"),
        member5_phone=request.form.get("member5_phone"),

        member6_name=request.form.get("member6_name"),
        member6_email=request.form.get("member6_email"),
        member6_branch=request.form.get("member6_branch"),
        member6_usn=request.form.get("member6_usn"),
        member6_phone=request.form.get("member6_phone"),
    )

    db.session.add(registration)
    db.session.commit()

    return redirect(url_for("thank_you"))

@app.route("/thank-you")
def thank_you():
    return render_template("thank-you.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
