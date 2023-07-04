import unittest
from src.chatbot import Chatbot
from src.user import User
from src.ai_tools import generate_recommendations, automate_management, analyze_data

class TestChatbot(unittest.TestCase):

    def setUp(self):
        self.user = User("user_id", "name", "investment_preferences", "risk_tolerance")
        self.chatbot = Chatbot()

    def test_welcome_message(self):
        self.assertEqual(self.chatbot.welcome_message(), "Welcome to our Real Estate Investment Platform!")

    def test_investment_recommendation_message(self):
        recommendations = generate_recommendations(self.user.user_id)
        self.assertEqual(self.chatbot.investment_recommendation_message(self.user.user_id), f"Based on your preferences, we recommend: {recommendations}")

    def test_investment_tracking_message(self):
        investment_status = automate_management(self.user.user_id)
        self.assertEqual(self.chatbot.investment_tracking_message(self.user.user_id), f"Your current investment status is: {investment_status}")

    def test_analytics_message(self):
        analytics = analyze_data(self.user.user_id)
        self.assertEqual(self.chatbot.analytics_message(self.user.user_id), f"Based on our analysis, here are some insights: {analytics}")

if __name__ == '__main__':
    unittest.main()