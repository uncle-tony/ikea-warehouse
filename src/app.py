from flask import Flask
from controller import api
from model import db
from commands import db_cli, translate_cli
from jaeger_client import Config
from flask_opentracing import FlaskTracing

def initialize_tracer():
    config = Config(
        config={ # usually read from some yaml config
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'local_agent': {
                'reporting_host': 'localhost',
                'reporting_port': '6831',
            },
            'logging': True,
        },
        service_name='ikea-warehouse',
        validate=True,
    )
    return config.initialize_tracer()

def create_app(config_object="config.ProductionConfig"):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_commands(app)
    return app

def register_extensions(app):
    db.init_app(app)
    api.init_app(app)
    # It is nopt possible to implement app factory schema > tracer.init(app)
    tracer = FlaskTracing(initialize_tracer, True, app)

    return None

def register_commands(app):
    app.cli.add_command(db_cli)
    app.cli.add_command(translate_cli)
    return None

app = create_app()

