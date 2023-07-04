```python
import ai_tools
from user import User
from investment import Investment
from property import Property
from reit import REIT
from chatbot import Chatbot

class TechnologyAutomation:
    def __init__(self):
        self.chatbot = Chatbot()

    def automate_investment_recommendations(self, user: User):
        recommendations = ai_tools.generate_recommendations(user.user_id)
        self.chatbot.send_message(user.user_id, "investment_recommendation_message", recommendations)

    def automate_investment_tracking(self, investment: Investment):
        tracking_info = ai_tools.automate_management(investment.investment_id)
        self.chatbot.send_message(investment.user_id, "investment_tracking_message", tracking_info)

    def automate_property_management(self, property: Property):
        management_info = ai_tools.automate_management(property.property_id)
        self.chatbot.send_message(property.owner_id, "property_management_message", management_info)

    def automate_reit_management(self, reit: REIT):
        management_info = ai_tools.automate_management(reit.reit_id)
        self.chatbot.send_message(reit.owner_id, "reit_management_message", management_info)

    def analyze_user_behavior(self, user: User):
        analytics = ai_tools.analyze_data(user.user_id)
        return analytics
```