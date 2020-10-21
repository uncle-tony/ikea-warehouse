from flask import Flask
from controller import api
from model import db
from commands import db_cli, translate_cli

def create_app(config_object="config.ProductionConfig"):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_commands(app)
    return app

def register_extensions(app):
    db.init_app(app)
    api.init_app(app)
    return None

def register_commands(app):
    app.cli.add_command(db_cli)
    app.cli.add_command(translate_cli)
    return None

app = create_app()

