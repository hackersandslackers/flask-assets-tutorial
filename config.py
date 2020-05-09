"""Flask configuration variables."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


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

