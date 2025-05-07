import pytest
from src.generators import filter_by_currency

def test_filter_by_currency(transactions_for_generators):
    generator = filter_by_currency(transactions_for_generators, 'USD')
    assert next(generator) == {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
    assert next(generator) == {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }

def test_filter_by_not_existing_currency(transactions_for_generators):
    assert filter_by_currency(transactions_for_generators, 'TRY') == 'Операции по данной валюте отсутствуют'

def test_filter_by_currency_empty():
    assert (filter_by_currency([{}], 'USD')) == 'Операции по данной валюте отсутствуют'