"""Compile static assets."""
from flask import current_app as app
from flask_assets import Bundle


def compile_static_assets(assets):
    """Configure and build asset bundles."""
    main_style_bundle = Bundle(
        'src/less/*.less',
        'main_bp/homepage.less',
        filters='less,cssmin',
        output='dist/css/landing.css',
        extra={'rel': 'stylesheet/css'}
    )  # Main Stylesheets Bundle
    main_js_bundle = Bundle(
        'src/js/main.js',
        filters='jsmin',
        output='dist/js/main.min.js'
    )  # Main JavaScript Bundle
    admin_style_bundle = Bundle(
        'src/less/*.less',
        'admin_bp/admin.less',
        filters='less,cssmin',
        output='dist/css/account.css',
        extra={'rel': 'stylesheet/css'}
    )  # Admin Stylesheets Bundle
    assets.register('main_styles', main_style_bundle)
    assets.register('main_js', main_js_bundle)
    assets.register('admin_styles', admin_style_bundle)
    if app.config['FLASK_ENV'] != 'production':
        main_style_bundle.build()
        main_js_bundle.build()
        admin_style_bundle.build()
    return assets
