from flask import Flask, request, render_template, session, flash
from currency import Currency
# from forex_python.converter import CurrencyRates
app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

currency = Currency()
@app.route("/")

def create_form():
    """Create home page with form"""
    return render_template('index.html')


@app.route("/convert")
def translate_currency():
    """Translate inputted currency codes into the appropriate dollar amounts"""
    start = request.args["start"]
    end = request.args["end"]
    amount = request.args["amount"]

    start_err, end_err, amount_err = currency.validate_code(start,end, amount)

    errors = []

    if start_err:
        errors.append(f"Not a valid currency code:\"{start}\" - please enter a valid currency code")
    if end_err:
        errors.append(f"Not a valid currency code:\"{end}\" - please enter a valid currency code")
    if amount_err:
        errors.append(f"Not a valid amount:\"{amount}\" - please enter a valid amount, perhaps remove non-decimal symbols (eg, $, +, -) and not enter more than one decimal")
    if len(errors) > 0:
        for error in errors:
            flash(error, 'error')
        return render_template("index.html")

    currency_name_start, symbol_and_amount_end, currency_name_end = currency.calculate_currency(start, end, amount)
    print(currency_name_end)  
    flash(f"{amount} {currency_name_start} ({start.upper()}) ", "success")
    return render_template("index2.html", amount = amount, start = start.upper(), end =end.upper(), currency_name_start =currency_name_start, symbol_and_amount_end = symbol_and_amount_end, currency_name_end = currency_name_end)







