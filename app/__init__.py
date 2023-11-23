"""
This module sets up a Flask application with SQLAlchemy and migration support.

It creates a Flask application instance, configures it using settings from 'config.py',
initializes a SQLAlchemy database instance, and sets up migration capabilities using Flask-Migrate.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes
