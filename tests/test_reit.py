import unittest
from src.reit import REIT

class TestREIT(unittest.TestCase):

    def setUp(self):
        self.reit = REIT("reit_id", "reit_name", "reit_value")

    def test_reit_id(self):
        self.assertEqual(self.reit.reit_id, "reit_id")

    def test_reit_name(self):
        self.assertEqual(self.reit.reit_name, "reit_name")

    def test_reit_value(self):
        self.assertEqual(self.reit.reit_value, "reit_value")

    def test_update_reit_value(self):
        self.reit.update_reit_value("new_reit_value")
        self.assertEqual(self.reit.reit_value, "new_reit_value")

if __name__ == '__main__':
    unittest.main()