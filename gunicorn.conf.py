"""Gunicorn configuration file."""
import socket
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

ENVIRONMENT = environ.get("ENVIRONMENT")

proc_name = "flaskassets"
wsgi_app = "wsgi:app"
bind = "unix:flask.sock"
threads = 4
workers = 2

if ENVIRONMENT == "development":
    reload = True
    workers = 1
    threads = 1

if ENVIRONMENT == "production":
    daemon = True
    accesslog = "/var/log/flaskassets/access.log"
    errorlog = "/var/log/flaskassets/error.log"
    loglevel = "trace"
    dogstatsd_tags = [
        "env:prod",
        f"host:{socket.gethostbyname(socket.gethostname())}",
        "service:flaskassets",
        "language:python",
    ]
