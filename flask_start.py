from flask import Flask, request

from utils import get_currency_exchange_rate

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p><b>Hello, World!</b></p>"


@app.route("/rates", methods=['GET'])
def get_rates():
    currency_a = request.args.get('currency_a', default='USD')
    currency_b = request.args.get('currency_b', default='UAH')
    result = get_currency_exchange_rate(currency_a, currency_b)
    return result
