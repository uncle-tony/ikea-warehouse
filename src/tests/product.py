from tests.base import BaseCase

class TestProduct(BaseCase):
    def test_product_v1(self):
        """ Check endpoint availability """
        response = self.app.get('/v.1/product')
        self.assertEqual(200, response.status_code)
    
    def test_product_v2(self):
        """ Check endpoint availability """
        response = self.app.get('/v.2/product')
        self.assertEqual(200, response.status_code)
