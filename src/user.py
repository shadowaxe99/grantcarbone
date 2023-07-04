```python
class User:
    def __init__(self, user_id, name, investment_preferences, risk_tolerance):
        self.user_id = user_id
        self.name = name
        self.investment_preferences = investment_preferences
        self.risk_tolerance = risk_tolerance

    def get_user_details(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "investment_preferences": self.investment_preferences,
            "risk_tolerance": self.risk_tolerance
        }

    def update_investment_preferences(self, new_preferences):
        self.investment_preferences = new_preferences

    def update_risk_tolerance(self, new_tolerance):
        self.risk_tolerance = new_tolerance
```