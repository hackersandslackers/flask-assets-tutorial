"""Routes for main pages."""
from flask import Blueprint, render_template

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates", static_folder="static")


@main_blueprint.route("/", methods=["GET"])
def home():
    """Homepage route."""
    return render_template(
        "index.jinja2", title="Home | Flask-Blueprint Tutorial", template="home-static main", body="Home"
    )


@main_blueprint.route("/about", methods=["GET"])
def about():
    """About page route."""
    return render_template(
        "index.jinja2", title="About | Flask-Blueprint Tutorial", template="about-static main", body="About"
    )


@main_blueprint.route("/etc", methods=["GET"])
def etc():
    """Etc page route."""
    return render_template(
        "index.jinja2", title="Etc | Flask-Blueprint Tutorial", template="etc-static main", body="Etc"
    )
