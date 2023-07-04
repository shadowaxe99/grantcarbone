```python
import datetime
from src.user import User
from src.property import Property
from src.reit import REIT

class Investment:
    def __init__(self, user: User, investment_type: str, investment_id: str, investment_amount: float, investment_date: datetime.date):
        self.user = user
        self.investment_type = investment_type
        self.investment_id = investment_id
        self.investment_amount = investment_amount
        self.investment_date = investment_date

    def get_investment_details(self):
        return {
            "user_id": self.user.user_id,
            "investment_type": self.investment_type,
            "investment_id": self.investment_id,
            "investment_amount": self.investment_amount,
            "investment_date": self.investment_date
        }

class PropertyInvestment(Investment):
    def __init__(self, user: User, property: Property, investment_amount: float, investment_date: datetime.date):
        super().__init__(user, "property", property.property_id, investment_amount, investment_date)
        self.property = property

    def get_investment_details(self):
        details = super().get_investment_details()
        details["property_details"] = self.property.get_property_details()
        return details

class REITInvestment(Investment):
    def __init__(self, user: User, reit: REIT, investment_amount: float, investment_date: datetime.date):
        super().__init__(user, "reit", reit.reit_id, investment_amount, investment_date)
        self.reit = reit

    def get_investment_details(self):
        details = super().get_investment_details()
        details["reit_details"] = self.reit.get_reit_details()
        return details
```