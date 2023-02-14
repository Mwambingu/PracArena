from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route("/")
def error():
  return "<h1>You are lost my friend. Welcome to the void</h1>"

@auth.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if user:
      if check_password_hash(user.password, password):
        flash("Logged in successfully!", category="success")
        login_user(user, remember=True)
        return redirect(url_for("views.home"))
      else:
        flash("Incorrect password! Try again.", category="error")
    else:
      flash("User does not exist!", category="error")
  return render_template("login.html", boolean=True)

@auth.route("logout")
def logout():
  return render_template("home.html")

@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
  if request.method == "POST":
    email = request.form.get('email')
    first_name = request.form.get('firstName')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    if len(email) <= 4:
      flash('Email must be greater than 4 characters.', category='error')
    elif len(first_name) <= 2:
      flash('First Name must be greater than 2 characters.', category='error')
    elif password1 != password2:
      flash('Passwords do not match.', category='error')
    elif len(password1) <= 7:
      flash('Password must be equal to 8 or more characters.', category='error')
    else:
      # Add user to db
      user = User.query.filter_by(email=email).first()
      if user:
        flash('User already exists. Use the Login page.', category="error")
      else:
        new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method="sha256"))
        db.session.add(new_user)
        db.session.commit()
        login_user(user, remember=True)
        flash("Account created!", category='success')
        return redirect(url_for('views.home'))

  return render_template("sign-up.html")
