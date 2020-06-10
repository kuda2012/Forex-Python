from unittest import TestCase
from flask import session, request
from app import app, currency
from currency import Currency
from unittest.mock import MagicMock
from forex_python.converter import CurrencyRates, CurrencyCodes
app.config['TESTING'] = True

class FlaskTests(TestCase):

    def test_USD(self):
        """Test to see if one USD translate to one USD"""
        with app.test_client() as client:
         
            params = {"start": "USD", "end": "USD", "amount": "1"}
            res = client.get("/convert", query_string=params)
            html = res.get_data(as_text=True)
            self.assertIn("1.00", html)
    
    def test_magic_mock(self):
        """Test to see if magic mock return value is used as amount"""
        with app.test_client() as client:
            currency.c.convert = MagicMock(return_value=3)
            params = {"start": "USD", "end": "GBP", "amount": "1"}
            res = client.get("/convert", query_string=params)
            html = res.get_data(as_text=True)
            self.assertIn("3.00", html)

    def test_Validate(self):
        cur = Currency()
        s, e, a = cur.validate_code("USD", "GBP", "1.0")
        self.assertFalse(s)
        self.assertFalse(e)
        self.assertFalse(a)

    def test_ValidateBadStart(self):
        cur = Currency()
        s, e, a = cur.validate_code("XXX", "GBP", "1.0")
        self.assertTrue(s)
        self.assertFalse(e)
        self.assertFalse(a)

    def test_ValidateBadStartEnd(self):
        cur = Currency()
        s, e, a = cur.validate_code("XXX", "YYY", "1.0")
        self.assertTrue(s)
        self.assertTrue(e)
        self.assertFalse(a)
    def test_ValidateBadStartEndAmount(self):
        cur = Currency()
        s, e, a = cur.validate_code("XXX", "YYY", "1..0")
        self.assertTrue(s)
        self.assertTrue(e)
        self.assertTrue(a)
