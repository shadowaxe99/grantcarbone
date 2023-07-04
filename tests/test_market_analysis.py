import unittest
from src import market_analysis

class TestMarketAnalysis(unittest.TestCase):

    def setUp(self):
        self.market_analysis = market_analysis.MarketAnalysis()

    def test_market_growth(self):
        growth_rate = self.market_analysis.calculate_growth_rate()
        self.assertIsInstance(growth_rate, float)
        self.assertGreater(growth_rate, 0)

    def test_investment_demand(self):
        demand = self.market_analysis.calculate_investment_demand()
        self.assertIsInstance(demand, int)
        self.assertGreater(demand, 0)

    def test_investment_efficiency(self):
        efficiency = self.market_analysis.calculate_investment_efficiency()
        self.assertIsInstance(efficiency, float)
        self.assertGreaterEqual(efficiency, 0)
        self.assertLessEqual(efficiency, 1)

    def test_personalized_experience(self):
        experience_score = self.market_analysis.evaluate_personalized_experience()
        self.assertIsInstance(experience_score, float)
        self.assertGreaterEqual(experience_score, 0)
        self.assertLessEqual(experience_score, 1)

if __name__ == '__main__':
    unittest.main()