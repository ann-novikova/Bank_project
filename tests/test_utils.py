import json
from unittest.mock import mock_open, patch

from src.utils import convert_file


def test_convert_file_not_found() -> None:
    assert convert_file("data.py") == []


def test_convert_file_incorrect_format() -> None:
    assert convert_file(r"C:\Users\user\PycharmProjects\Bank_project\src\decorators.py") == []


def test_convert_file_not_file() -> None:
    assert convert_file("hello") == []


def test_convert_file_incorrect_json(incorrect_json: list) -> None:
    with patch("builtins.open", mock_open(read_data=str(incorrect_json))) as mock_file:
        assert convert_file("builtins.open") == []
        mock_file.assert_called_once_with("builtins.open", "r", encoding="utf-8")


def test_convert_file_correct(correct_path: str) -> None:
    with open(correct_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    assert convert_file(correct_path) == data
