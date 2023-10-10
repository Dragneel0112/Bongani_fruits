#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.fruit import Fruits
from models.user import User
from os import environ
from flask import Flask, render_template
import uuid
app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
