import unittest
from app import create_app

class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here

    def setUp(self):
        app = create_app()
        self.app = app.test_client()

    def test_exchane_rate(self):
        query_string = {'source': 'USD', 'target': 'JPY', 'amount': '100'}
        response = self.app.get('/exchane_rate', query_string=query_string)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"msg": "success", "amount": "10,800.00"})


if __name__ == '__main__':
    unittest.main()
