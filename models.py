from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Registration(db.Model):
    __tablename__ = "registration"  # Changed to match app.py

    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(200), nullable=False)  # Ensure team_name is present and required

    # Member 1 (required)
    member1_name = db.Column(db.String(100), nullable=False)
    member1_email = db.Column(db.String(120), nullable=False)  # Changed length to 120
    member1_usn = db.Column(db.String(20))  # Changed length to 20, made optional
    member1_phone = db.Column(db.String(15))  # Changed length to 15
    member1_branch = db.Column(db.String(50), nullable=False)

    # Member 2–6 (optional)
    member2_name = db.Column(db.String(100))
    member2_email = db.Column(db.String(120))  # Changed length to 120
    member2_usn = db.Column(db.String(20))     # Changed length to 20
    member2_phone = db.Column(db.String(15))   # Changed length to 15
    member2_branch = db.Column(db.String(50))

    member3_name = db.Column(db.String(100))
    member3_email = db.Column(db.String(120))
    member3_usn = db.Column(db.String(20))
    member3_phone = db.Column(db.String(15))
    member3_branch = db.Column(db.String(50))

    member4_name = db.Column(db.String(100))
    member4_email = db.Column(db.String(120))
    member4_usn = db.Column(db.String(20))
    member4_phone = db.Column(db.String(15))
    member4_branch = db.Column(db.String(50))

    member5_name = db.Column(db.String(100))
    member5_email = db.Column(db.String(120))
    member5_usn = db.Column(db.String(20))
    member5_phone = db.Column(db.String(15))
    member5_branch = db.Column(db.String(50))

    member6_name = db.Column(db.String(100))
    member6_email = db.Column(db.String(120))
    member6_usn = db.Column(db.String(20))
    member6_phone = db.Column(db.String(15))
    member6_branch = db.Column(db.String(50))

    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)