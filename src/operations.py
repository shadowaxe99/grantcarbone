```python
from src.user import User
from src.investment import Investment
from src.property import Property
from src.reit import REIT
from src.ai_tools import AI_Tools
from src.chatbot import Chatbot
from src.data_analytics import Data_Analytics
from src.partnerships import Partnership
from src.scalability import Scalability

class Operations:
    def __init__(self):
        self.users = []
        self.investments = []
        self.properties = []
        self.reits = []
        self.ai_tools = AI_Tools()
        self.chatbot = Chatbot()
        self.data_analytics = Data_Analytics()
        self.partnerships = []
        self.scalability = Scalability()

    def add_user(self, user_id, name, investment_preferences, risk_tolerance):
        user = User(user_id, name, investment_preferences, risk_tolerance)
        self.users.append(user)

    def add_investment(self, investment_id, property_id, reit_id, investment_amount, investment_date):
        investment = Investment(investment_id, property_id, reit_id, investment_amount, investment_date)
        self.investments.append(investment)

    def add_property(self, property_id, property_type, property_value, rental_income):
        property = Property(property_id, property_type, property_value, rental_income)
        self.properties.append(property)

    def add_reit(self, reit_id, reit_name, reit_value):
        reit = REIT(reit_id, reit_name, reit_value)
        self.reits.append(reit)

    def add_partnership(self, partner_id, partner_type, partnership_date):
        partnership = Partnership(partner_id, partner_type, partnership_date)
        self.partnerships.append(partnership)

    def generate_recommendations(self, user_id):
        return self.ai_tools.generate_recommendations(user_id)

    def automate_management(self, investment_id):
        return self.ai_tools.automate_management(investment_id)

    def analyze_data(self, user_id):
        return self.data_analytics.analyze_data(user_id)

    def expand_offerings(self):
        return self.scalability.expand_offerings()

    def hire_personnel(self, role):
        return self.scalability.hire_personnel(role)

    def establish_partnership(self, partner_id):
        return self.scalability.establish_partnership(partner_id)
```