from cs50 import SQL
from flask import flash, redirect, render_template, session
from functools import wraps

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///users.db")


def apology(message, code=400):
    """Render message as an apology to user."""
    return render_template("apology.html", code=code, message=message), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


def send_user_data(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        users = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])

        if len(users) == 0:
            session.clear()
            flash("Your session has expired. Please login again!", "info")
            return redirect("/login")
        return f(*args, **kwargs, user=users[0])

    return decorated_function