class Config():
    SQLALCHEMY_DATABASE_URI = "postgresql://ikea:ikea@localhost/ikea"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    ENV = "production"
    DEBUG = False
    FLASK_RUN_PORT = 9000
