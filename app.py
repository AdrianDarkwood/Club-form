from flask import Flask, request, render_template
import psycopg2, os

app = Flask(__name__)
DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    return psycopg2.connect(DATABASE_URL)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")

    if not name or not email:
        return "Missing name or email", 400

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO registrations (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    cur.close()
    conn.close()

    return render_template("thank-you.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
