# ==========================================================
# Electricity Consumption Analytics using Flask + Tableau
# Developed by Pranavi
# ==========================================================

from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    request,
    session,
    flash
)

from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

# ==========================================================
# Flask Configuration
# ==========================================================

app = Flask(__name__)

app.secret_key = "electricity_consumption_pranavi_2026"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ==========================================================
# Database Model
# ==========================================================

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    def __repr__(self):

        return f"<User {self.username}>"

# ==========================================================
# Create Database
# ==========================================================

with app.app_context():

    db.create_all()

# ==========================================================
# Helper Function
# ==========================================================

def is_logged_in():

    return "user_id" in session

# ==========================================================
# Home Page
# ==========================================================

@app.route("/")

def home():

    if not is_logged_in():

        return redirect(url_for("login"))

    return render_template("home.html")

# ==========================================================
# About Page
# ==========================================================

@app.route("/about")

def about():

    if not is_logged_in():

        return redirect(url_for("login"))

    return render_template("about.html")
# ==========================================================
# Register
# ==========================================================

@app.route("/register", methods=["GET", "POST"])

def register():

    if is_logged_in():

        return redirect(url_for("home"))

    if request.method == "POST":

        username = request.form["username"].strip()

        password = request.form["password"]

        if len(username) < 3:

            flash(
                "Username must contain at least 3 characters.",
                "danger"
            )

            return render_template("register.html")

        if len(password) < 6:

            flash(
                "Password must contain at least 6 characters.",
                "danger"
            )

            return render_template("register.html")

        existing_user = User.query.filter_by(
            username=username
        ).first()

        if existing_user:

            flash(
                "Username already exists.",
                "warning"
            )

            return render_template("register.html")

        hashed_password = generate_password_hash(password)

        new_user = User(

            username=username,

            password=hashed_password

        )

        db.session.add(new_user)

        db.session.commit()

        flash(

            "Registration Successful. Please Login.",

            "success"

        )

        return redirect(url_for("login"))

    return render_template("register.html")


# ==========================================================
# Login
# ==========================================================

@app.route("/login", methods=["GET", "POST"])

def login():

    if is_logged_in():

        return redirect(url_for("home"))

    if request.method == "POST":

        username = request.form["username"].strip()

        password = request.form["password"]

        user = User.query.filter_by(

            username=username

        ).first()

        if user and check_password_hash(

            user.password,

            password

        ):

            session["user_id"] = user.id

            session["username"] = user.username

            flash(

                f"Welcome {user.username}!",

                "success"

            )

            return redirect(url_for("home"))

        flash(

            "Invalid Username or Password",

            "danger"

        )

        return render_template("login.html")

    return render_template("login.html")


# ==========================================================
# Logout
# ==========================================================

@app.route("/logout")

def logout():

    session.clear()

    flash(

        "You have logged out successfully.",

        "info"

    )

    return redirect(url_for("login"))
# ==========================================================
# Dashboard 1
# ==========================================================

@app.route("/dashboard1")
def dashboard1():

    if not is_logged_in():

        return redirect(url_for("login"))

    return render_template("dashboard1.html")


# ==========================================================
# Dashboard 2
# ==========================================================

@app.route("/dashboard2")
def dashboard2():

    if not is_logged_in():

        return redirect(url_for("login"))

    return render_template("dashboard2.html")


# ==========================================================
# Dashboard 3
# ==========================================================

@app.route("/dashboard3")
def dashboard3():

    if not is_logged_in():

        return redirect(url_for("login"))

    return render_template("dashboard3.html")


# ==========================================================
# Tableau Story
# ==========================================================

@app.route("/story")
def story():

    if not is_logged_in():

        return redirect(url_for("login"))

    return render_template("story.html")


# ==========================================================
# User Profile (Optional)
# ==========================================================

@app.route("/profile")
def profile():

    if not is_logged_in():

        return redirect(url_for("login"))

    return render_template(

        "profile.html",

        username=session.get("username")

    )


# ==========================================================
# Contact (Optional)
# ==========================================================

@app.route("/contact")
def contact():

    if not is_logged_in():

        return redirect(url_for("login"))

    return render_template("contact.html")
# ==========================================================
# Error Handling
# ==========================================================
# ==========================================================
# Context Processor
# ==========================================================

@app.context_processor
def inject_user():

    return {

        "logged_in": is_logged_in(),

        "username": session.get("username")

    }


# ==========================================================
# Prevent Browser Cache
# ==========================================================

@app.after_request
def add_header(response):

    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"

    response.headers["Pragma"] = "no-cache"

    response.headers["Expires"] = "0"

    return response


# ==========================================================
# Run Flask Application
# ==========================================================

if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )
