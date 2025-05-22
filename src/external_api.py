import os
from dotenv import load_dotenv
import requests
import datetime
from typing import NoReturn


def convert_currency(transaction: dict) -> (float | NoReturn):
    """Функцию, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    try:
        currency_from = transaction.get('operationAmount')['currency']['code']
        currency_amount = transaction.get('operationAmount')['amount']
        date = (datetime.datetime.strptime(transaction.get('date')[:10], "%Y-%m-%d")).strftime("%Y-%m-%d")

    except Exception:
        raise ValueError('Not found key')

    local_currency = 'RUB'

    if currency_from == local_currency:
        return float(currency_amount)

    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {
        "amount": currency_amount,
        "from": currency_from,
        "to": local_currency,
        "date": date
    }
    load_dotenv()
    headers = {
        "apikey": os.getenv('API_KEY')
    }

    response = requests.get(url, headers=headers, params=payload)

    if response.status_code != 200:
        raise ValueError('Failed to get currency rate')
    currency_data = response.json()

    return currency_data.get('result')

