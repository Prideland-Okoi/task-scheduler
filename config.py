import os


class Config:
    # Flask app configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'sqlite:///scheduler.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-Bootstrap configuration (if used)
    BOOTSTRAP_SERVE_LOCAL = True

    # Flask-WTF configuration (if using Flask-WTF for forms)
    WTF_CSRF_SECRET_KEY = "a_secret_key_for_csrf_protection"

    # Additional app-specific configuration
    # ...
