from cs50 import SQL
from datetime import timedelta
from flask import Flask, redirect, render_template, request
from flask_session import Session


# Configure the application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=7) # Set session lifetime to 7 days
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///users.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template("layout.html")


''' User Account Routes '''

@app.route("/account")
def account():
    return render_template("account.html")


''' User Authentication Routes '''

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register the user"""
    if request.method == "POST":
        return "Success"

    else:
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Login the user"""
    if request.method == "POST":
        return redirect("/")
    
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Forgot user and log out"""
    session.clear()

    return redirect("/")


# Run application
if __name__ == "__main__":
    app.run(debug=True)