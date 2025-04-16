from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=31)

fake_users = {
    "admin": {"password": "password", "email": "a@aaa"},
    "user": {"password": "password", "email": "b@aaa"},
    "guest": {"password": "password", "email": "c@aaa"}
}


@app.route("/")
def index():
    if session.get("username"):
        return render_template("index.html", username=session["username"])
    return render_template("index.html")


@app.get("/login")
def login_form():
    return render_template("login.html")


@app.post("/login")
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username in fake_users and fake_users[username]["password"] == password:
        session["username"] = username
        return redirect(url_for("index"))
    return render_template("index.html", error="Invalid credentials")


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        if username in fake_users:
            return render_template("register.html", error="Username already exists")
        fake_users[username] = {"password": password, "email": email}
        return redirect(url_for("index"))
