from cs50 import SQL
from datetime import timedelta
from flask import Flask, render_template


# Configure the application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=7) # Set session lifetime to 7 days
Session(app)

# Configure CS50 Library to use SQLite database
db.execute("sqlite:///users.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template("index.html")


# Run application
if __name__ == "__main__":
    app.run(debug=True)