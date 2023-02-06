#!/usr/bin/env python3

from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

flask_app = Flask(__name__)
flask_auth = HTTPBasicAuth()

users  = {
        "john": generate_password_hash("hello"),
        "susan": generate_password_hash("bye")
}

@flask_auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
                return username

@flask_app.route('/')
@flask_auth.login_required
def index():
    return "Hello, {}!".format(flask_auth.current_user())


if __name__ == '__main__':
    flask_app.run()
