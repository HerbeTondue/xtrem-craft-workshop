from python.src.bank import Bank
from python.src.currency import Currency

class BankBuilder:
    def __init__(self) -> None:
        self._currency_init  = Currency.EUR;
        self._currency_final = Currency.USD;
        self._exchange_rates = 1.2;
    
    def with_currency_init(self, currency_init: Currency) -> "BankBuilder":
        self._currency_init = currency_init
        return self
        
    def with_currency_final(self, currency_final: Currency) -> "BankBuilder":
        self._currency_final = currency_final
        return self
    
    def with_exchange_rates(self, exchange_rates: float) -> "BankBuilder":
        self._exchange_rates = exchange_rates
        return self
    
    def build(self) -> Bank:
        return Bank.create_bank(self._currency_init, self._currency_final, self._exchange_rates)