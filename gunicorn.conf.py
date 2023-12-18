"""Gunicorn configuration file."""
import socket

from config import Config

proc_name = "flaskassets"
wsgi_app = "wsgi:app"
bind = "unix:flask.sock"
threads = 4
workers = 2

if Config.ENVIRONMENT == "development":
    reload = True
    workers = 1
    threads = 1


if Config.ENVIRONMENT == "production":
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
