"""Initialize app."""
from flask import Flask
from flask_assets import Environment


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    assets = Environment()
    assets.init_app(app)

    # Initialize plugins
    assets.init_app(app)

    with app.app_context():
        # Import parts of our application
        from .admin import admin_routes
        from .main import main_routes
        from .assets import compile_static_assets

        # Register Blueprints
        app.register_blueprint(admin_routes.admin_bp)
        app.register_blueprint(main_routes.main_bp)

        # Compile static assets
        compile_static_assets(assets)

        return app
