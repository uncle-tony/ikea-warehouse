from flask import abort, request
from flask_restful import Resource

from model.v2.product import ProductV2
from model.v2.article import ArticleV2
from model import db

import json

ALLOWED_ACTIONS = ['sell']

class ClientControllerV2(Resource):
    def post(self):
        def _rollback(start, product_list):
            start-=1
            while start >= 0:
                article_roll = ArticleV2.query.filter_by(art_id=product_list.articles[start]['art_id']).first()
                if article_roll:
                    try:
                        article_roll.update(stock=article_roll.stock+int(product_list.articles[start]['stock']))
                        start-=1
                    except:
                        print("Unable to recover article {} to original value".format(article_roll.name))

        params = json.loads(request.data)
        if params['action'] and params['action'] in ALLOWED_ACTIONS:
            product = ProductV2.query.filter_by(name=params['product']).first()
            if product:
                try:
                    update_counter = 0
                    for idx, article in enumerate(product.articles):
                        article_ref = ArticleV2.query.filter_by(art_id=article['art_id']).first()
                        if article_ref:
                            new_stock = int(article_ref.stock)-int(article['amount_of'])
                            if new_stock >= 0:
                                try:
                                    article_ref.update(stock=article_ref.stock-int(article['amount_of']))
                                    update_counter+=1
                                except:
                                    print("Unable to update {} article".format(article['art_id']))
                                    _rollback(idx, product)
                            else:
                                _rollback(idx, product)
                                abort(404, description="No stock available for this product")
                    if len(product.articles) == update_counter:
                        product.delete()
                        return {'success': True}
                    else:
                        return {'success': False}
                except:
                    abort(400, description="Bad request")
            else:
                abort(400, description="Bad request")
        else:
            abort(400, description="Bad request")
