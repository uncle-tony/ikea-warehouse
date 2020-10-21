from flask import abort, request
from flask_restful import Resource

from model.v1.article import ArticleV1
from model import db

import json

ALLOWED_EXTENSIONS = ['json']

def allowed_filename(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

class ArticleControllerV1(Resource):
    def post(self):
        """ Handle upload JSON file with inventary """
        submitted_file = request.files["file"]
        if submitted_file and allowed_filename(submitted_file.filename):
            try:
                article_list = json.loads(submitted_file.read())
                for article in article_list["inventory"]:
                    try:
                        sql_article = ArticleV1(art_id=int(article["art_id"]), name=article["name"], stock=int(article["stock"]))
                        sql_article.save()
                    except Exception as err3:
                        print(err3)
                return {'success': True}
            except Exception as err2:
                abort(400, description=err2)
        else:
            abort(400, description="Invalid input file")
