from flask import Flask

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'g5iN88SaNBpeU1K77R1sQwOjfzOUxEmF'

  return app