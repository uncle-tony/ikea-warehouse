from flask_restful import Api
# API v1
from controller.v1.article import ArticleControllerV1
from controller.v1.product import ProductControllerV1
from controller.v1.client import ClientControllerV1
# API v2
from controller.v2.article import ArticleControllerV2
from controller.v2.product import ProductControllerV2
from controller.v2.client import ClientControllerV2

api = Api()
# API v1
api.add_resource(ArticleControllerV1, '/v.1/article')
api.add_resource(ProductControllerV1, '/v.1/product')
api.add_resource(ClientControllerV1, '/v.1/client')
# API v2
api.add_resource(ArticleControllerV2, '/v.2/article')
api.add_resource(ProductControllerV2, '/v.2/product')
api.add_resource(ClientControllerV2, '/v.2/client')
