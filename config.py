"""Flask configuration variables."""
from os import environ
from dotenv import load_dotenv


load_dotenv()


class Config:

    # General
    FLASK_ENV = environ.get('FLASK_ENV')
    FLASK_DEBUG = 'wsgi.py'
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    # Flask-Assets
    LESS_BIN = '/usr/local/bin/lessc'
    ASSETS_DEBUG = False
    ASSETS_AUTO_BUILD = True

