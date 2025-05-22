import datetime
import os
from typing import NoReturn

import requests
from dotenv import load_dotenv


def convert_currency(transaction: dict) -> float | NoReturn:
    """Функцию, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    operation_amount = transaction.get("operationAmount")
    if not isinstance(operation_amount, dict):
        raise ValueError("Not found key")

    currency = operation_amount.get("currency")
    if not isinstance(currency, dict):
        raise ValueError("Not found key")

    currency_code = currency.get("code")
    if not isinstance(currency_code, str):
        raise ValueError("Not found key")

    amount = operation_amount.get("amount")
    if not isinstance(amount, (int, float, str)):
        raise ValueError("Not found key")

    date_str = transaction.get("date")
    if not isinstance(date_str, str):
        raise ValueError("Not found key")

    currency_from = currency_code
    currency_amount = amount
    date = (datetime.datetime.strptime(date_str[:10], "%Y-%m-%d")).strftime("%Y-%m-%d")

    local_currency = "RUB"

    if currency_from == local_currency:
        return float(currency_amount)

    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {"amount": currency_amount, "from": currency_from, "to": local_currency, "date": date}
    load_dotenv()
    headers = {"apikey": os.getenv("API_KEY")}

    response = requests.get(url, headers=headers, params=payload)

    if response.status_code != 200:
        raise ValueError("Failed to get currency rate")
    currency_data = response.json()

    return currency_data.get("result")
