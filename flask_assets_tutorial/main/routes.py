"""Routes for main pages."""
from flask import Blueprint, render_template

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates", static_folder="static")


@main_blueprint.route("/", methods=["GET"])
def home():
    """Home page route."""
    return render_template(
        "index.jinja2",
        title="Home",
        body="Welcome to the Flask-Assets tutorial demo!",
        template="home-static main",
        logged_in=False,
    )


@main_blueprint.route("/about", methods=["GET"])
def about():
    """About page route."""
    return render_template(
        "index.jinja2",
        title="About",
        body="At HackersAndSlackers, we pride ourselves in stuff. That's why work tirelessly to build and deliver stuff, 24/7.",
        template="about-static main",
        logged_in=False,
    )


@main_blueprint.route("/etc", methods=["GET"])
def etc():
    """Etc page route."""
    return render_template(
        "index.jinja2",
        title="Etc.",
        body="Here's a third page, for good measure.",
        template="etc-static main",
        logged_in=False,
    )
