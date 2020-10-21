from model import db

class ArticleV2(db.Model):
    art_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def __init__(self, art_id, name, stock):
        self.art_id = art_id
        self.name = name
        self.stock = stock

    def __repr__(self):
        return f'ArticleV2({self.art_id}, {self.name}, {self.stock})'

    def __str__(self):
        return self.name

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as ex:
            raise ex

    def update(self, art_id=None, name=None, stock=None):
        try:
            if art_id:
                self.art_id = art_id
            if name:
                self.name = name
            if stock:
                self.stock = stock
            db.session.commit()
        except Exception as ex:
            raise ex

