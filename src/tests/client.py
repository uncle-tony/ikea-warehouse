from tests.base import BaseCase
from werkzeug.datastructures import FileStorage

import io, os

class TestClient(BaseCase):
    def test_client_v1(self):
        """ Check endpoint availability """
        f = FileStorage (
            stream = open(os.path.join("tests/data/inventory.json"), 'rb'),
            filename = 'inventory.json',
            content_type = 'application/json'
        )
        self.app.post('/v.1/article', data = {
            'file': f 
        }, content_type='multipart/form-data')
        f = FileStorage (
            stream = open(os.path.join("tests/data/products.json"), 'rb'),
            filename = 'products.json',
            content_type = 'application/json'
        )
        self.app.post('/v.1/product', data = {
            'file': f 
        }, content_type='multipart/form-data')
        response = self.app.post('/v.1/client', data = '''{
            "action": "sell",
            "product": "Dining Chair"
        }''', content_type='application/json')
        self.assertEqual(200, response.status_code)
    
    def test_client_v2(self):
        """ Check endpoint availability """
        f = FileStorage (
            stream = open(os.path.join("tests/data/inventory.json"), 'rb'),
            filename = 'inventory.json',
            content_type = 'application/json'
        )
        self.app.post('/v.2/article', data = {
            'file': f 
        }, content_type='multipart/form-data')
        f = FileStorage (
            stream = open(os.path.join("tests/data/products.json"), 'rb'),
            filename = 'products.json',
            content_type = 'application/json'
        )
        self.app.post('/v.2/product', data = {
            'file': f 
        }, content_type='multipart/form-data')
        response = self.app.post('/v.2/client', data = '''{
            "action": "sell",
            "product": "Dining Chair"
        }''', content_type='application/json')
        self.assertEqual(200, response.status_code)
