import os
from unittest.mock import mock_open, patch

import pytest

from src.read_files import read_csv_file, read_excel_file

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_read_csv_file_with_mock(csv_excel_file: str, expected_data: list[dict]) -> None:
    with patch("builtins.open", mock_open(read_data=csv_excel_file)) as mock_file:
        assert read_csv_file("test.csv") == expected_data
        mock_file.assert_called_once_with("test.csv", "r", encoding="utf-8")


def test_read_csv_file_real_file() -> None:
    assert read_csv_file(os.path.join(ROOT_DIR, "data", "transactions.csv"))[:2] == [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 3598919.0,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]


def test_read_csv_file_empty() -> None:
    with pytest.raises(ValueError, match="Путь к файлу не указан"):
        read_csv_file()


def test_read_excel_file_real() -> None:
    assert read_excel_file(os.path.join(ROOT_DIR, "data", "transactions_excel.xlsx"))[:2] == [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 3598919.0,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]


def test_read_excel_file_empty() -> None:
    with pytest.raises(ValueError, match="Путь к файлу не указан"):
        read_excel_file()
