import pytest

from src.search import count_by_category, search_string


@pytest.mark.parametrize(
    "search_word, expected",
    [
        (
            "карты",
            [
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                }
            ],
        ),
        ("Отмена", []),
        (
            "СЧЕТ",
            [
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                },
            ],
        ),
    ],
)
def test_search_string(transactions_for_generators: list[dict], search_word: str, expected: list[dict]) -> None:
    assert search_string(transactions_for_generators, search_word) == expected


@pytest.mark.parametrize(
    "list_category, expected",
    [
        (["Перевод организации"], {"Перевод организации": 2}),
        (["Перевод с карты на карту"], {"Перевод с карты на карту": 1}),
        (["Перевод со счета на счет", "Отмена"], {"Перевод со счета на счет": 2, "Отмена": 0}),
        ([], {}),
    ],
)
def test_count_by_category(transactions_for_generators, list_category, expected) -> None:
    assert count_by_category(transactions_for_generators, list_category) == expected
