import unittest
from unittest.mock import patch
from src import technology_automation as ta

class TestTechnologyAutomation(unittest.TestCase):

    @patch('src.ai_tools.generate_recommendations')
    def test_generate_recommendations(self, mock_generate_recommendations):
        user_id = 1
        mock_generate_recommendations.return_value = ['Property1', 'REIT1']
        result = ta.generate_recommendations(user_id)
        self.assertEqual(result, ['Property1', 'REIT1'])
        mock_generate_recommendations.assert_called_once_with(user_id)

    @patch('src.ai_tools.automate_management')
    def test_automate_management(self, mock_automate_management):
        investment_id = 1
        mock_automate_management.return_value = True
        result = ta.automate_management(investment_id)
        self.assertEqual(result, True)
        mock_automate_management.assert_called_once_with(investment_id)

    @patch('src.ai_tools.analyze_data')
    def test_analyze_data(self, mock_analyze_data):
        user_id = 1
        mock_analyze_data.return_value = {'investment_preference': 'Commercial'}
        result = ta.analyze_data(user_id)
        self.assertEqual(result, {'investment_preference': 'Commercial'})
        mock_analyze_data.assert_called_once_with(user_id)

    @patch('src.chatbot.send_message')
    def test_send_welcome_message(self, mock_send_message):
        user_id = 1
        mock_send_message.return_value = True
        result = ta.send_welcome_message(user_id)
        self.assertEqual(result, True)
        mock_send_message.assert_called_once_with(user_id, 'welcome_message')

    @patch('src.chatbot.send_message')
    def test_send_investment_recommendation_message(self, mock_send_message):
        user_id = 1
        mock_send_message.return_value = True
        result = ta.send_investment_recommendation_message(user_id)
        self.assertEqual(result, True)
        mock_send_message.assert_called_once_with(user_id, 'investment_recommendation_message')

    @patch('src.chatbot.send_message')
    def test_send_investment_tracking_message(self, mock_send_message):
        user_id = 1
        mock_send_message.return_value = True
        result = ta.send_investment_tracking_message(user_id)
        self.assertEqual(result, True)
        mock_send_message.assert_called_once_with(user_id, 'investment_tracking_message')

if __name__ == '__main__':
    unittest.main()