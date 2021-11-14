import requests
import json
from flask import Flask, render_template
from requests.exceptions import HTTPError

from models.exchangerates import ExchangeRate
from models.rates import Rate


def get_available_currency():
    currencies = set()
    for table in ('A', 'B', 'C'):
        url = f'http://api.nbp.pl/api/exchangerates/tables/{table}'
        resp = requests.get(url)
        only_json = json.loads(resp.text)[0]
        exchangerate = ExchangeRate(**only_json)
        currencies = currencies | set(rate.code for rate in exchangerate.rates)
    return currencies


def get_actual_rate_by_code(code):
    for table in ('A', 'B', 'C'):
        url = f'http://api.nbp.pl/api/exchangerates/rates/{table}/{code}'
        try:
            resp = requests.get(url)
            resp.raise_for_status()
        except HTTPError:
            continue
        only_json = json.loads(resp.text)
        rate = Rate(**only_json)
        return rate.rates[0].mid


app = Flask(__name__, template_folder='templates')


@app.route('/currencies')
def available_currency():
    currency_codes = get_available_currency()
    return render_template('all_rates.html', codes=currency_codes)


@app.route('/currency/<code>/actual-rate')
def get_actual_rate(code):
    actual_rate = get_actual_rate_by_code(code)
    return render_template('actual_rate.html', code=code, rate=actual_rate)


if __name__ == '__main__':
    app.run(debug=True)
