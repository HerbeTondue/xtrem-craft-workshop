from python.src.portfolio import Portfolio
from python.src.money import Money
from python.src.currency import Currency

class TestPortfolio:
    
    def test_add_money_in_same_currency_in_portfolio(self):
        # Arrange
        portfolio: Portfolio = Portfolio({Currency.EUR: 1.0})
        amount = Money(5.0, Currency.EUR)

        # Act
        Portfolio.add_money_in_portfolio(portfolio, amount)

        # Assert
        assert Portfolio.get_value(portfolio, Currency.EUR) == 6.0
    
    def test_add_money_in_empty_portfolio(self):
        # Arrange
        portfolio2: Portfolio = Portfolio({})
        amount2 = Money(5.0, Currency.EUR)

        # Act
        Portfolio.add_money_in_portfolio(portfolio2, amount2)

        # Assert
        assert Portfolio.get_value(portfolio2, Currency.EUR) == 5.0

    def test_get_value(self):
        # Arrange
        portfolio: Portfolio = Portfolio({Currency.EUR: 1.0})
        currency: Currency = Currency.EUR

        # Act
        value = Portfolio.get_value(portfolio, currency)
        
        # Assert
        assert value == 1.0

    # def test_evaluate_portfolio(self):
    #     # Arrange
    #     portfolio: Portfolio
    #     # Act
    #     Portfolio.evaluate_portfolio(portfolio)

    #     # Assert
    #     assert isinstance(Portfolio.evaluate_portfolio(5, 10), float)
    #     assert Portfolio.evaluate_portfolio(5, 10) == 50