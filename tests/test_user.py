import unittest
from src import user

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user1 = user.User("user_id_1", "John Doe", "residential", "medium")
        self.user2 = user.User("user_id_2", "Jane Doe", "commercial", "high")

    def test_user_creation(self):
        self.assertEqual(self.user1.user_id, "user_id_1")
        self.assertEqual(self.user1.name, "John Doe")
        self.assertEqual(self.user1.investment_preferences, "residential")
        self.assertEqual(self.user1.risk_tolerance, "medium")

        self.assertEqual(self.user2.user_id, "user_id_2")
        self.assertEqual(self.user2.name, "Jane Doe")
        self.assertEqual(self.user2.investment_preferences, "commercial")
        self.assertEqual(self.user2.risk_tolerance, "high")

    def test_user_update(self):
        self.user1.update_investment_preferences("commercial")
        self.assertEqual(self.user1.investment_preferences, "commercial")

        self.user2.update_risk_tolerance("low")
        self.assertEqual(self.user2.risk_tolerance, "low")

if __name__ == '__main__':
    unittest.main()