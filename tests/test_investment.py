```python
import unittest
from src import investment

class TestInvestment(unittest.TestCase):

    def setUp(self):
        self.user_data = {
            "user_id": "123",
            "name": "John Doe",
            "investment_preferences": "Commercial",
            "risk_tolerance": "High"
        }
        self.investment_data = {
            "investment_id": "456",
            "property_id": "789",
            "reit_id": "101112",
            "investment_amount": 100000,
            "investment_date": "2022-01-01"
        }

    def test_create_investment(self):
        result = investment.create_investment(self.user_data, self.investment_data)
        self.assertEqual(result['investment_id'], self.investment_data['investment_id'])

    def test_get_investment(self):
        investment.create_investment(self.user_data, self.investment_data)
        result = investment.get_investment(self.investment_data['investment_id'])
        self.assertEqual(result['investment_id'], self.investment_data['investment_id'])

    def test_update_investment(self):
        investment.create_investment(self.user_data, self.investment_data)
        updated_data = self.investment_data.copy()
        updated_data['investment_amount'] = 200000
        result = investment.update_investment(updated_data)
        self.assertEqual(result['investment_amount'], updated_data['investment_amount'])

    def test_delete_investment(self):
        investment.create_investment(self.user_data, self.investment_data)
        result = investment.delete_investment(self.investment_data['investment_id'])
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
```