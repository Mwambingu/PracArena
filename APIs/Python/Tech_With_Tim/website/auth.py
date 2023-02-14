from flask import Blueprint, render_template, request

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

@auth.route("sign-up", methods=["GET", "POST"])
def sign_up():
  return render_template("sign-up.html")
