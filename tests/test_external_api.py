from unittest.mock import Mock, patch

import pytest

from src.external_api import convert_currency


def test_convert_currency_success(transaction_for_api: dict) -> None:
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "date": "2018-02-22",
        "historical": "",
        "info": {"rate": 81.972231, "timestamp": 1519328414},
        "query": {"amount": 8221.37, "from": "USD", "to": "RUB"},
        "result": 673924.04078,
        "success": True,
    }

    with patch("requests.get", return_value=mock_response):
        result = convert_currency(transaction_for_api)
        assert result == 673924.04078


def test_convert_local_currency() -> None:
    assert (
        convert_currency(
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        )
        == 31957.58
    )


def test_convert_currency_no_currency(transaction_for_api: dict) -> None:
    mock_response = Mock()
    mock_response.status_code = 500

    with patch("requests.get", return_value=mock_response):
        with pytest.raises(ValueError, match="Failed to get currency rate"):
            convert_currency(transaction_for_api)


@pytest.mark.parametrize(
    "transaction",
    [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37"},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
    ],
)
def test_convert_currency_incorrect_transaction(transaction: dict) -> None:
    with pytest.raises(ValueError, match="Not found key"):
        convert_currency(transaction)
