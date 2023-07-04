import unittest
from src.property import Property

class TestProperty(unittest.TestCase):

    def setUp(self):
        self.property = Property("property_id", "property_type", "property_value", "rental_income")

    def test_property_id(self):
        self.assertEqual(self.property.property_id, "property_id")

    def test_property_type(self):
        self.assertEqual(self.property.property_type, "property_type")

    def test_property_value(self):
        self.assertEqual(self.property.property_value, "property_value")

    def test_rental_income(self):
        self.assertEqual(self.property.rental_income, "rental_income")

    def test_calculate_return_on_investment(self):
        self.property.property_value = 100000
        self.property.rental_income = 10000
        self.assertEqual(self.property.calculate_return_on_investment(), 0.1)

if __name__ == '__main__':
    unittest.main()