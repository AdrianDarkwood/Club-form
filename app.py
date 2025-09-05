from flask import Flask, render_template, request, redirect, url_for
import os
from sqlalchemy import inspect
from models import db, Registration
from functools import wraps

app = Flask(__name__)

# Database configuration
database_url = os.getenv("DATABASE_URL")
if database_url:
    # Render provides postgres://; SQLAlchemy needs postgresql://
    database_url = database_url.replace("postgres://", "postgresql://", 1)
else:
    # Local fallback for development
    database_url = "sqlite:///local.db"

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Bind SQLAlchemy instance from models.py
db.init_app(app)

# ✅ Create tables (no-op if they already exist)
with app.app_context():
    db.create_all()

def _unauthorized_response():
    return ("Unauthorized", 401, {"WWW-Authenticate": "Basic realm=Registration Admin"})

def require_basic_auth(view_func):
    @wraps(view_func)
    def wrapped(*args, **kwargs):
        admin_user = os.getenv("ADMIN_USERNAME")
        admin_pass = os.getenv("ADMIN_PASSWORD")

        if not admin_user or not admin_pass:
            return ("Admin credentials not configured", 403)

        auth = request.authorization
        if not auth or auth.type != "basic":
            return _unauthorized_response()

        if auth.username != admin_user or auth.password != admin_pass:
            return _unauthorized_response()

        return view_func(*args, **kwargs)
    return wrapped

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    registration = Registration(
        team_name=request.form["team_name"],  # Added team_name to form handling
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

@app.route("/admin")
@require_basic_auth
def admin_dashboard():
    registrations = Registration.query.order_by(Registration.submitted_at.desc()).all()
    return render_template("admin.html", registrations=registrations)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
