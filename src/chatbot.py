```python
from ai_tools import generate_recommendations, automate_management, analyze_data

class Chatbot:
    def __init__(self, user_id):
        self.user_id = user_id

    def welcome_message(self):
        return f"Welcome to our Real Estate Investment Platform, User {self.user_id}!"

    def investment_recommendation_message(self):
        recommendations = generate_recommendations(self.user_id)
        return f"Based on your preferences, we recommend these investments: {recommendations}"

    def investment_tracking_message(self):
        investment_status = automate_management(self.user_id)
        return f"Here is the status of your investments: {investment_status}"

    def handle_user_query(self, query):
        if "recommendation" in query:
            return self.investment_recommendation_message()
        elif "track investment" in query:
            return self.investment_tracking_message()
        else:
            return "Sorry, I didn't understand that. Can you please rephrase?"

    def provide_support(self, query):
        try:
            response = self.handle_user_query(query)
            return response
        except Exception as e:
            return f"Sorry, an error occurred: {str(e)}"
```