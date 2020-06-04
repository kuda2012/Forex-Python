from unittest import TestCase
from flask import session, request
from app import app
from currency import Currency


app.config['TESTING'] = True

class FlaskTests(TestCase):

    def test_USD(self):
        """Test to see if one USD translate to one USD"""
        with app.test_client() as client:
         
            params = {"start": "USD", "end": "USD", "amount": "2"}
            res = client.get("/convert", query_string=params)
            html = res.get_data(as_text=True)
            self.assertIn("2.00", html)