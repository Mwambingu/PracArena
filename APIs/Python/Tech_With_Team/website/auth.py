from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route("login")
def login():
  return "<h1>LOGIN</h1>"

@auth.route("logout")
def logout():
  return "<h1>LOGOUT</h1>"

@auth.route("sign-up")
def sign_up():
  return "<h1>SIGN UP</h1>"