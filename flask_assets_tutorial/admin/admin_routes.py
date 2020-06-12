"""Routes for logged-in account pages."""
from flask import Blueprint, render_template


admin_bp = Blueprint(
    'admin_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@admin_bp.route('/dashboard', methods=['GET'])
def dashboard():
    """Admin dashboard route."""
    return render_template(
        'dashboard.jinja2',
        title='Admin Dashboard | Flask-Blueprint Tutorial',
        template='dashboard-static account',
        body="Account"
    )
