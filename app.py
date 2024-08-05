from cs50 import SQL
from datetime import timedelta
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from apps.helpers import apology, login_required


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
@app.route("/account/dashboard")
@login_required
def account():
    return render_template("account.html")


''' User Authentication Routes '''

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register the user"""
    if request.method == "POST":
        # Get Form Data
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirmPassword = request.form.get('confirmPassword')
        otp = request.form.get('otp')

        # TO DO: Validate form data

        # TO DO: Sanitize form data, e.g, remove spaces

        # Hash the password
        password = generate_password_hash(password)

        # Register the user to the database
        db.execute('INSERT INTO users(fname, lname, username, email, password) VALUES(?, ?, ?, ?, ?)', fname, lname, username, email, password)

        # Forgot any users previously logged in
        session.clear()

        # Get the id of this user
        users = db.execute("SELECT id FROM users WHERE email = ?", email)

        # Login in the user to the session
        session["user_id"] = users[0]['id']

        # Greet user for the first time
        flash("Welcome " + fname + "!", "success")
        return redirect("/account")

    else:
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Login the user"""
    if request.method == "POST":
        # Get the Form data
        email = request.form.get('email')
        password = request.form.get('password')

        # TO DO: Validate Form Data

        # Login in user
        users = db.execute('SELECT id FROM users WHERE email = ?', email)

        # Forget any previews user_id
        session.clear()

        # Remember which user has logged in
        session["user_id"] = users[0]["id"]
        return redirect("/account")

    
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Forgot user and log out"""
    session.clear()
    flash("You have been logged out!", "info")
    return redirect("/account")


# Run application
if __name__ == "__main__":
    app.run(debug=True)