```python
import requests
import json

class MarketAnalysis:
    def __init__(self):
        self.api_url = "https://api.realestateanalysis.com"  # hypothetical API

    def get_market_data(self):
        response = requests.get(f"{self.api_url}/market_data")
        data = json.loads(response.text)
        return data

    def analyze_market_growth(self, market_data):
        growth_rate = (market_data['current_value'] - market_data['previous_value']) / market_data['previous_value']
        return growth_rate

    def analyze_investment_demand(self, market_data):
        demand_rate = market_data['investment_demand'] / market_data['total_investments']
        return demand_rate

    def analyze_investment_efficiency(self, market_data):
        efficiency_rate = market_data['successful_investments'] / market_data['total_investments']
        return efficiency_rate

    def perform_market_analysis(self):
        market_data = self.get_market_data()
        growth_rate = self.analyze_market_growth(market_data)
        demand_rate = self.analyze_investment_demand(market_data)
        efficiency_rate = self.analyze_investment_efficiency(market_data)

        analysis_results = {
            "growth_rate": growth_rate,
            "demand_rate": demand_rate,
            "efficiency_rate": efficiency_rate
        }

        return analysis_results
```