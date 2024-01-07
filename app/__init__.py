from app import routes
from flask import Flask, Blueprint
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from config import Config
from app.models import db


def create_app():
    app = Flask(__name__, template_folder="../templates")
    app.config.from_object(Config)

    # Initialize SQLAlchemy and Migrate
    db.init_app(app)
    migrate = Migrate(app, db)

    # Initialize Bootstrap for easy styling
    bootstrap = Bootstrap(app)

    # Import and register blueprints
    from app.routes import task
    app.register_blueprint(task)

    return app

#
