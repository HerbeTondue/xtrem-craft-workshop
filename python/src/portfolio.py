from .currency import Currency

class Portfolio:

    def __init__(self, list_currency = {}) -> None:
        self.list_currency = list_currency
        
    def add_money_in_portfolio (self, amount : dict[float, Currency]) -> None:

        # if (self == {}):
        #     self.list_currency[list(self.list_currency)[0]] = list(amount)[1]
        #     self.list_currency[list(self.list_currency)[1]] = list(amount)[0]
        #     print(self.list_currency)
        
        # else:
        if (amount.get(list(amount)[0]) == list(self.list_currency)[0]):
            self.list_currency[list(self.list_currency)[0]] += list(amount)[0]
        print(self.list_currency)
    
    def get_value(self, currency : Currency) -> None:
        return self.list_currency.get(currency)
    
    def evaluate_portfolio ():
        return