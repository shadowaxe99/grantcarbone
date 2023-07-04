```python
from src.ai_tools import generate_recommendations, automate_management
from src.user import User
from src.investment import Investment
from src.property import Property
from src.reit import REIT

class ServiceOffering:
    def __init__(self):
        self.users = []
        self.investments = []
        self.properties = []
        self.reits = []

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

    def provide_recommendations(self, user_id):
        user = next((user for user in self.users if user.user_id == user_id), None)
        if user:
            return generate_recommendations(user)
        else:
            return "User not found."

    def automate_investment_management(self, investment_id):
        investment = next((investment for investment in self.investments if investment.investment_id == investment_id), None)
        if investment:
            return automate_management(investment)
        else:
            return "Investment not found."
```