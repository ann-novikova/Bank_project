import os
from dotenv import load_dotenv
import requests
import datetime


def convert_currency(transaction: dict) -> (float | bool):
    try:
        currency_from = transaction.get('operationAmount')['currency']['code']
        currency_amount = transaction.get('operationAmount')['amount']
        date = (datetime.datetime.strptime(transaction.get('date')[:10], "%Y-%m-%d")).strftime("%Y-%m-%d")

    except Exception:
        print("Not find key[s]")
        return False

    local_currency = 'RUB'

    if currency_from == local_currency:
        return currency_amount

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
        return False
    currency_data = response.json()

    return currency_data.get('result')

