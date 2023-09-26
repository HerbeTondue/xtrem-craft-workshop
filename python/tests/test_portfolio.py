

from python.src.portfolio import Portfolio
from python.src.currency import Currency

class TestPortfolio:
    
    def test_add_money_in_same_currency_in_portfolio(self):
        # Arrange
        portfolio: Portfolio = Portfolio({Currency.EUR: 1.0})
        amount = {5.0 : Currency.EUR}

        # Act
        Portfolio.add_money_in_portfolio(portfolio, amount)
        # Assert
        assert Portfolio.get_value(portfolio, Currency.EUR) == 6.0


    # def test_evaluate_portfolio(self):
    #     # Arrange
    #     portfolio: Portfolio
    #     # Act

    #     # Assert
    #     # assert isinstance(Portfolio.evaluate_portfolio(5, 10), float)
    #     # assert Portfolio.evaluate_portfolio(5, 10) == 50