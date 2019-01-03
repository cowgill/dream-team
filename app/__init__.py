
# third-party imports
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment, Bundle

from .views.home import home

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    # setup assets environments
    assets = Environment(app)

    # compile & combine all sass files into one css file.
    scss = Bundle('scss/foo.scss', 'scss/bar.scss', filters='pyscss', output='css/style.css')

    # register the new css file so we can use in templates.
    assets.register('scss_all', scss)

    # register the blueprints
    app.register_blueprint(home)

    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/403.html', title='Forbidden'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html', title='Page Not Found'), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('errors/500.html', title='Server Error'), 500

    return app