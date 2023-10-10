import pytest

from python.src.bank import Bank
from python.src.currency import Currency
from python.src.money import Money
from python.src.missing_exchange_rate_error import MissingExchangeRateError
from .test_data_builder import BankBuilder


class TestBank:
    def test_convert_currency_euro_to_usd_returns_right_amount(self):
        #Arrange
        bankbuilder = BankBuilder().with_currency_init(Currency.EUR).with_currency_final(Currency.USD).with_exchange_rates(1.2).build()
        money_initial = Money(10, Currency.EUR)
        currency_final = Currency.USD
        
        # Act
        result = bankbuilder.convert_currency(money_initial, currency_final)
        print(f'money currency {money_initial.currency}, currency {currency_final}')
        #Assert
        assert result == 12
    

    def test_convert_currency_euro_to_usd_returns_same_value(self):
        # Arrange
        bankbuilder = BankBuilder().with_currency_init(Currency.EUR).with_currency_final(Currency.EUR).with_exchange_rates(1.2).build()
        money_initial = Money(10, Currency.EUR)
        currency_final = Currency.EUR
        
        # Act
        result = bankbuilder.convert_currency(money_initial, currency_final)
        
        # Assert
        assert result == 10
        
    def test_convert_currency_with_missing_exchange_rate_throws_exception(self):
        with pytest.raises(MissingExchangeRateError) as error:
            #Arrange
            bankbuilder = BankBuilder().with_currency_init(Currency.EUR).with_currency_final(Currency.USD).with_exchange_rates(1.2).build()
            
            money_initial = Money(10, Currency.EUR)
            currency_final = Currency.KRW
            
            #Act

            bankbuilder.convert_currency(money_initial, currency_final)
            
        #Assert
        assert str(error.value) == "EUR->KRW"

    def test_convert_currency_with_different_exchange_rate_returns_different_floats(self):
        # Arrange
        bankbuilder = BankBuilder().with_currency_init(Currency.EUR).with_currency_final(Currency.USD).with_exchange_rates(1.2).build()
        money_initial = Money(10, Currency.EUR)
        currency_final = Currency.USD
        
        # Act
        result = bankbuilder.convert_currency(money_initial, currency_final)
        
        # Assert
        assert result == 12
        
        #Act
        bankbuilder.add_exchange_rate(Currency.EUR, Currency.USD, exchange_rate = 1.3)
        
        #Assert
        assert bankbuilder.convert_currency(money_initial, Currency.USD) == 13


