import unittest
from src import main

class TestMain(unittest.TestCase):

    def setUp(self):
        self.app = main.app.test_client()
        self.app.testing = True 

    def test_home_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_user_profile(self):
        result = self.app.get('/user_profile')
        self.assertEqual(result.status_code, 200)

    def test_investment_list(self):
        result = self.app.get('/investment_list')
        self.assertEqual(result.status_code, 200)

    def test_property_list(self):
        result = self.app.get('/property_list')
        self.assertEqual(result.status_code, 200)

    def test_reit_list(self):
        result = self.app.get('/reit_list')
        self.assertEqual(result.status_code, 200)

    def test_chatbot_interface(self):
        result = self.app.get('/chatbot_interface')
        self.assertEqual(result.status_code, 200)

    def test_analytics_dashboard(self):
        result = self.app.get('/analytics_dashboard')
        self.assertEqual(result.status_code, 200)

if __name__ == "__main__":
    unittest.main()