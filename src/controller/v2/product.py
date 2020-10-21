from flask import abort, request
from flask_restful import Resource

from model.v2.product import ProductV2, ProductSchemaV2
from model import db

import json

ALLOWED_EXTENSIONS = ['json']

def allowed_filename(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

class ProductControllerV2(Resource):
    def get(self):
        schema = ProductSchemaV2(many=True)
        return schema.dump(ProductV2.query.all())

    def post(self):
        """ Handle upload JSON file with inventary """
        submitted_file = request.files["file"]
        if submitted_file and allowed_filename(submitted_file.filename):
            try:
                product_list = json.loads(submitted_file.read())
                for product in product_list["products"]:
                    try:
                        sql_product = ProductV2(name=product["name"], articles=product["contain_articles"])
                        sql_product.save()
                    except Exception as err3:
                        print(err3)
                return {'success': True}
            except Exception as err2:
                abort(400, description=err2)
        else:
            abort(400, description="Invalid input file")
