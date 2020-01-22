from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

db = SQLAlchemy()


def create_app(env=None):
    from app.config import config_by_name, version
    from app.routes import register_routes

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "test"])
    api = Api(app, title="Flask Interview API", version=version)

    register_routes(api, app, version)
    db.init_app(app)

    return app
