from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os
from .db import db, migrate
from .routes.user_routes import bp as user_bp


def create_app(config=None):
    # Load environment variables from .env file if not in production
    if os.getenv('FLASK_ENV') != 'production':
        load_dotenv()

    app = Flask(__name__)
    CORS(app)

    URI = os.getenv('DATABASE_URL') or os.getenv('SQLALCHEMY_DATABASE_URI')

    # Fix for Heroku's postgres:// URL format
    if URI and URI.startswith("postgres://"):
        URI = URI.replace("postgres://", "postgresql://", 1)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = URI
    
    if config:
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(user_bp)

    return app
