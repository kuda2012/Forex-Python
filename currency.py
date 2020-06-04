from forex_python.converter import CurrencyRates, CurrencyCodes
from decimal import *

class Currency():
    def __init__(self):
        self.c = CurrencyRates()
        self.currency_codes = self.c.get_rates('USD').keys()
        self.symbols = CurrencyCodes()
    

    def validate_code(self, start, end, amount):
        """Return entered currency code if the input is invalid"""
        start_err = False
        end_err = False
        amount_err = False

        if start.upper() not in self.currency_codes:
            start_err = True
        if end.upper() not in self.currency_codes:
            end_err = True
        try:
            Decimal(amount)
        except:
            amount_err = True
        return start_err, end_err, amount_err

    def calculate_currency(self, start, end, amount):
        """Calculate the currency and return the currency with its given symbol"""
        start = start.upper()
        end =end.upper()
        converted_amount = self.c.convert(start, end, Decimal(amount))
        converted_amount = '%.2f' % converted_amount
        symbol = self.symbols.get_symbol(end)
        currency_name_start = self.symbols.get_currency_name(start)
        currency_name_end = self.symbols.get_currency_name(end)
        symbol_and_amount = symbol + " " + converted_amount
        return currency_name_start, symbol_and_amount, currency_name_end
