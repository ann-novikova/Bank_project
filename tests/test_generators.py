import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_correct(transactions_for_generators):
    generator = filter_by_currency(transactions_for_generators, "USD")
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


def test_filter_by_not_existing_currency(transactions_for_generators):
    with pytest.raises(ValueError):
        filter_by_currency(transactions_for_generators, "TRY")


def test_filter_by_currency_empty():
    with pytest.raises(ValueError):
        filter_by_currency([{}], "USD")


def test_transaction_descriptions_correct(transactions_for_generators):
    assert list(transaction_descriptions(transactions_for_generators)) == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


@pytest.mark.parametrize(
    "transaction, expected",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "info": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ],
            None,
        ),
        ([{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}], None),
    ],
)
def test_transaction_descriptions_mistakes(transaction, expected):
    assert next(transaction_descriptions(transaction)) == expected


def test_transaction_descriptions_empty():
    with pytest.raises(StopIteration):
        next(transaction_descriptions([]))


def test_card_number_generator_correct():
    generator = card_number_generator(10000, 10005)
    assert next(generator) == "0000 0000 0001 0000"
    assert next(generator) == "0000 0000 0001 0001"
    assert next(generator) == "0000 0000 0001 0002"
    assert next(generator) == "0000 0000 0001 0003"
    assert next(generator) == "0000 0000 0001 0004"


@pytest.mark.parametrize("start_num, stop_num", [(10, 5), (-100, -5), (0, 2)])
def test_card_number_generator_incorrect(start_num, stop_num):
    with pytest.raises(ValueError):
        next(card_number_generator(start_num, stop_num))
