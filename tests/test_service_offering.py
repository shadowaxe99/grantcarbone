import unittest
from unittest.mock import patch
from src import service_offering

class TestServiceOffering(unittest.TestCase):

    @patch('src.service_offering.generate_recommendations')
    def test_generate_recommendations(self, mock_generate_recommendations):
        mock_generate_recommendations.return_value = [{'investment_id': '123', 'property_id': '456', 'reit_id': '789'}]
        user_data = {'user_id': '1', 'name': 'John Doe', 'investment_preferences': 'Residential', 'risk_tolerance': 'High'}
        result = service_offering.generate_recommendations(user_data)
        self.assertEqual(result, [{'investment_id': '123', 'property_id': '456', 'reit_id': '789'}])

    @patch('src.service_offering.get_investment_opportunities')
    def test_get_investment_opportunities(self, mock_get_investment_opportunities):
        mock_get_investment_opportunities.return_value = [{'property_id': '456', 'property_type': 'Residential', 'property_value': '500000', 'rental_income': '2000'}]
        result = service_offering.get_investment_opportunities()
        self.assertEqual(result, [{'property_id': '456', 'property_type': 'Residential', 'property_value': '500000', 'rental_income': '2000'}])

    @patch('src.service_offering.automate_management')
    def test_automate_management(self, mock_automate_management):
        mock_automate_management.return_value = True
        investment_data = {'investment_id': '123', 'property_id': '456', 'reit_id': '789', 'investment_amount': '100000', 'investment_date': '2021-01-01'}
        result = service_offering.automate_management(investment_data)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()