#!/usr/bin/env python3

from flask import Flask, request, make_response
from functools import wraps


app = Flask(__name__)

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == 'username1' and auth.password == 'password':
            return f(*args, **kwargs)
        return make_response('Could not verify!', 401, {'www-Authenticate' : 'Basic realm="Login Required"'})
    return decorated

@app.route('/')
@auth_required
def index():
    return '<h1> You are logged in</h1>'

@app.route('/page')
@auth_required
def page():
    return '<h1> You are logged in</h1>'

if __name__ == ('__main__'):
    app.run(debug=True)