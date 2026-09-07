from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.config import Config

db = SQLAlchemy()


def create_app():
    
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    from app.routes import books_bp
    app.register_blueprint(books_bp)

    @app.route("/")
    def home():
        return "Book Library API is running"

    return app