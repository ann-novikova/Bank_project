import datetime
import os
from typing import NoReturn

import requests
from dotenv import load_dotenv

url = "https://api.apilayer.com/exchangerates_data/convert"
load_dotenv()
API_KEY = os.getenv("API_KEY")


def convert_currency(transaction: dict) -> float | NoReturn:
    """Функцию, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    try:
        operation_amount = transaction["operationAmount"]
        currency = operation_amount["currency"]
        currency_code = currency["code"]
        amount = operation_amount["amount"]
        date_str = transaction["date"]
    except (KeyError, TypeError, AttributeError):
        raise ValueError("Not found key")

    currency_from = currency_code
    currency_amount = amount
    date = (datetime.datetime.strptime(date_str[:10], "%Y-%m-%d")).strftime("%Y-%m-%d")

    local_currency = "RUB"

    if currency_from == local_currency:
        return float(currency_amount)

    payload = {"amount": currency_amount, "from": currency_from, "to": local_currency, "date": date}
    headers = {"apikey": API_KEY}

    response = requests.get(url, headers=headers, params=payload)

    if response.status_code != 200:
        raise ValueError("Failed to get currency rate")
    currency_data = response.json()

    return currency_data.get("result")
