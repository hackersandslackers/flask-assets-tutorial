"""Flask configuration variables."""
from os import environ, path

from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    """Set Flask configuration from .env file."""

    # General Config
    ENVIRONMENT = environ.get("ENVIRONMENT")

    # Flask Config
    FLASK_APP = "wsgi.py"
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_DEBUG = environ.get("FLASK_DEBUG")
    SOCK_SERVER_OPTIONS = {"ping_interval": 25}

    # Flask-Assets
    LESS_BIN = environ.get("LESS_BIN")
    ASSETS_DEBUG = True
    LESS_RUN_IN_DEBUG = True

    # Static Assets
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    COMPRESSOR_DEBUG = True
