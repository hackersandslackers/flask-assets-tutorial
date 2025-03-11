"""Routes for logged-in account pages."""

from flask import Blueprint, render_template

from log import LOGGER

admin_blueprint = Blueprint("admin_blueprint", __name__, template_folder="templates", static_folder="static")


@admin_blueprint.route("/dashboard", methods=["GET"])
def dashboard():
    """Admin dashboard route."""
    LOGGER.info("Admin dashboard rendered by user.")
    return render_template(
        "dashboard.jinja2",
        title="Admin Dashboard",
        template="dashboard-static account",
        body="This is the admin dashboard.",
        logged_in=True,
    )
