"""
This module configures the SQLAlchemy database URI based on the environment.
If the Flask environment is set to 'testing', it uses an in-memory SQLite database,
otherwise, it retrieves the SQLAlchemy database URI from the environment variables.
"""
import os
from dotenv import load_dotenv

load_dotenv()

if os.environ.get('FLASK_ENV') == 'testing':
    SQLALCHEMY_DATABASE_URI = 'sqlite:///memory:'
else:
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

SQLALCHEMY_TRACK_MODIFICATIONS = False
