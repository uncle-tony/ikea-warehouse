from model import db
from model.v2.article import ArticleV2
from sqlalchemy.dialects.postgresql import JSONB
from marshmallow import Schema, fields

class ArticleSchemaV2(Schema):
    art_id = fields.Str()
    amount_of = fields.Str()

class ProductSchemaV2(Schema):
    name = fields.Str()
    price = fields.Float()
    articles = fields.List(fields.Nested(ArticleSchemaV2))

class ProductV2(db.Model):
    prod_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    articles = db.Column(JSONB, nullable=False)

    def __init__(self, name, articles, price=100.0):
        self.name = name
        self.price = price
        self.articles = articles

    def __repr__(self):
        return f'ProductV2({self.name}, {self.price}, {self.articles})'

    def __str__(self):
        return self.name
    
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as ex:
            raise ex

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as ex:
            raise ex
