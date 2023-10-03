from .currency import Currency

class Money:
    
    def __init__(self, amount = 0.0, currency = {Currency}) -> None:
        self.currency = currency
        self.amount = amount