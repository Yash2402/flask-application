from flask import Blueprint, flash, render_template, request

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@auth.route("/logout")
def logout():
    return "<p>Successfully Logged Out</p>"


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        lastName = request.form.get("lastName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(str(email)) < 4:
            flash("Email must be longer than 3 characters.", category="error")
        elif len(str(firstName)) < 2 or len(str(lastName)) < 2:
            flash("Name must be longer than 1 character.", category="error")
        elif password1 != password2:
            flash("Password don't match", category="error")
        elif len(str(password1)) < 9:
            flash("Password must be longer than 8 characters.", category="error")
        else:
            flash("Account created!", category="success")

    return render_template("sign_up.html")
