"""Initialize Flask app."""
from flask import Flask
from flask_assets import Environment


def create_app():
    """Construct core Flask app."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    assets = Environment()

    # Initialize plugins
    assets.init_app(app)

    with app.app_context():
        # Import parts of our flask_assets_tutorial
        from .admin import routes as admin_routes
        from .assets import compile_js_assets, compile_stylesheet_bundles
        from .main import routes as main_routes

        # Register Blueprints
        app.register_blueprint(admin_routes.admin_blueprint)
        app.register_blueprint(main_routes.main_blueprint)

        # Compile static assets
        compile_stylesheet_bundles(assets)
        compile_js_assets(assets)

        return app
