```python
class Property:
    def __init__(self, property_id, property_type, property_value, rental_income):
        self.property_id = property_id
        self.property_type = property_type
        self.property_value = property_value
        self.rental_income = rental_income

    def get_property_details(self):
        return {
            "property_id": self.property_id,
            "property_type": self.property_type,
            "property_value": self.property_value,
            "rental_income": self.rental_income
        }

    def update_property_value(self, new_value):
        self.property_value = new_value

    def update_rental_income(self, new_income):
        self.rental_income = new_income
```