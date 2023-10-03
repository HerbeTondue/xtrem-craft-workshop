from .currency import Currency
from .money import Money

class Portfolio:

    def __init__(self, list_currency = {}) -> None:
        self.list_currency = list_currency
        
    def add_money_in_portfolio (self, money : Money) -> None:

        if (self.list_currency == {}):
            self.list_currency[money.currency] = money.amount
            return self.list_currency
        
        if (money.currency == list(self.list_currency)[0]):
            self.list_currency[list(self.list_currency)[0]] += money.amount
            return self.list_currency
            
    def get_value(self, currency : Currency) -> None:
        return self.list_currency.get(currency)
    
    # def evaluate_portfolio(self) -> None:
        
    #     return