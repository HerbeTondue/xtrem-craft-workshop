import pytest

from python.src.bank import Bank
from python.src.currency import Currency
from python.src.money import Money
from python.src.missing_exchange_rate_error import MissingExchangeRateError


class TestBank:
    def test_convert_currency_euro_to_usd_returns_right_amount(self):
        #Arrange
        exchange_rate = 1.2
        bank: Bank = Bank.create_bank(Currency.EUR, Currency.USD, exchange_rate)
        money_initial = Money(10, Currency.EUR)
        currency_final = Currency.USD
        
        # Act
        result = bank.convert_currency(money_initial, currency_final)
        print(f'money currency {money_initial.currency}, cureency {currency_final}')
        #Assert
        assert result == 12
    

    def test_convert_currency_euro_to_usd_returns_same_value(self):
        # Arrange
        exchange_rate = 1.2
        bank: Bank = Bank.create_bank(Currency.EUR, Currency.USD, exchange_rate)
        money_initial = Money(10, Currency.EUR)
        currency_final = Currency.EUR
        
        # Act
        result = bank.convert_currency(money_initial, currency_final)
        
        # Assert
        assert result == 10
        
    def test_convert_currency_with_missing_exchange_rate_throws_exception(self):
        with pytest.raises(MissingExchangeRateError) as error:
            #Arrange
            exchange_rate = 1.2
            bank: Bank = Bank.create_bank(Currency.EUR, Currency.USD, exchange_rate)
            
            money_initial = Money(10, Currency.EUR)
            currency_final = Currency.KRW
            
            #Act

            bank.convert_currency(money_initial, currency_final)
            
        #Assert
        assert str(error.value) == "EUR->KRW"

    def test_convert_currency_with_different_exchange_rate_returns_different_floats(self):
        # Arrange
        exchange_rate = 1.2
        bank: Bank = Bank.create_bank(Currency.EUR, Currency.USD, exchange_rate)
        money_initial = Money(10, Currency.EUR)
        currency_final = Currency.USD
        
        # Act
        result = bank.convert_currency(money_initial, currency_final)
        
        # Assert
        assert result == 12
        
        #Act
        bank.add_exchange_rate(Currency.EUR, Currency.USD, exchange_rate = 1.3)
        
        #Assert
        assert bank.convert_currency(money_initial, Currency.USD) == 13


