"""Compile static assets."""
from flask import current_app as app
from flask_assets import Bundle, Environment


def compile_stylesheet_bundles(assets: Environment) -> Environment:
    """
    Create minified CSS bundles from LESS styles.

    :param Environment assets: Flask `environment` for static assets.

    :returns: Environment
    """
    # Main Stylesheets Bundle
    main_style_bundle = Bundle(
        "src/less/*.less",
        "main_blueprint/homepage.less",
        filters="less,cssmin",
        output="dist/css/landing.css",
        extra={"rel": "stylesheet/css"},
    )
    # Admin Stylesheets Bundle
    admin_style_bundle = Bundle(
        "src/less/*.less",
        "admin_blueprint/admin.less",
        filters="less,cssmin",
        output="dist/css/account.css",
        extra={"rel": "stylesheet/css"},
    )
    assets.register("main_styles", main_style_bundle)
    assets.register("admin_styles", admin_style_bundle)
    if app.config["ENVIRONMENT"] == "development":
        main_style_bundle.build()
        admin_style_bundle.build()
    return assets


def compile_static_assets(assets: Environment) -> Environment:
    """
    Create minified JS bundles from raw Javascript files.

    :param Environment assets: Flask `environment` for static assets.

    :returns: Environment
    """
    main_js_bundle = Bundle("src/js/main.js", filters="jsmin", output="dist/js/main.min.js")  # Main JavaScript Bundle
    assets.register("main_js", main_js_bundle)
    if app.config["ENVIRONMENT"] != "production":
        main_js_bundle.build()
    return assets
