import unittest
import app

class TestGoGameAPI(unittest.TestCase):
    def setUp(self):
        app.app.testing = True
        self.client = app.app.test_client()

    def test_responses(self):
        test_cases = [
            ('/0/0/0', {'max_draws': 0}),
            ('/1/1/2', {'max_draws': 2}),
            ('/3/4/5', {'max_draws': 6}),
            ('/3/3/3', {'max_draws': -1})
        ]

        for endpoint, expected in test_cases:
            with self.subTest(endpoint=endpoint):
                response = self.client.get(endpoint)
                self.assertEqual(response.json, expected)

if __name__ == '__main__':
    unittest.main()
