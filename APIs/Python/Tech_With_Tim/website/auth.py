from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route("/")
def error():
  return "<h1>You are lost my friend. Welcome to the void</h1>"

@auth.route("/login", methods=["GET", "POST"])
def login():
  data = request.form
  print(data)
  return render_template("login.html", boolean=True)

@auth.route("logout")
def logout():
  return render_template("home.html")

@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
  if request.method == "POST":
    email = request.form.get('email')
    firstName = request.form.get('firstName')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    if len(email) <= 4:
      flash('Email must be greater than 4 characters.', category='error')
    elif len(firstName) <= 2:
      flash('First Name must be greater than 2 characters.', category='error')
    elif password1 != password2:
      flash('Passwords do not match.', category='error')
    elif len(password1) <= 7:
      flash('Password must be equal to 8 or more characters.', category='error')
    else:
      # Add user to db
      flash("Account created!", category='success')

  return render_template("sign-up.html")
