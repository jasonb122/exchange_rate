import unittest
from app import create_app
from flask_testing import TestCase
import json

class MyTestCase(TestCase):
    def create_app(self):
        app = create_app()
        return app
    def test_exchane_rate(self):
        app = self.create_app()
        with self.app.test_client() as client:

            query_string = {'source': 'USD', 'target': 'JPY', 'amount': '100'}

            response = client.get('/exchane_rate', query_string=query_string)
            response_data = response.data.decode('utf-8')

            #回傳狀態碼是否為200
            self.assertEqual(response.status_code, 200)
            #回傳內容是否為預期結果
            self.assertEqual(json.loads(response_data), {'msg': 'success', 'amount': '11,180.10'})
            # print(response.json)

    def test_exchane_rate_missing_parameters(self):
        app = self.create_app()
        with self.app.test_client() as client:

            query_string = {'source': 'USD', 'target': 'JPY'}

            response = client.get('/exchane_rate', query_string=query_string)
            response_data = response.data.decode('utf-8')

            #回傳內容是否為預期結果
            self.assertEqual(json.loads(response_data), {'error': 'Missing parameters'})

    def test_exchane_rate_invalid_amount(self):
        app = self.create_app()
        with self.app.test_client() as client:

            query_string = {'source': 'USD', 'target': 'JPY', 'amount': 'test'}

            response = client.get('/exchane_rate', query_string=query_string)
            response_data = response.data.decode('utf-8')

            #回傳內容是否為預期結果
            self.assertEqual(json.loads(response_data), {'error': 'Invalid amount'})
if __name__ == '__main__':
    unittest.main()
