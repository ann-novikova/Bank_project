import pytest
from requests import patch
import pandas as pd
from unittest.mock import patch, mock_open
from src.read_files import read_csv_file, read_excel_file


def test_read_csv_file(csv_excel_file: str, expected_data: list[dict]) -> None:
    with patch("builtins.open", mock_open(read_data=csv_excel_file)) as mock_file:
        assert read_csv_file("builtins.open") == expected_data
        mock_file.assert_called_once_with("builtins.open", "r", encoding="utf-8")

def test_read_csv_file_empty() -> None:
    with pytest.raises(ValueError, match="Путь к файлу не указан"):
        read_csv_file()

def test_read_excel_file(expected_data: list[dict]) -> None:
    expected_data = pd.DataFrame(expected_data)
    with patch("pandas.read_excel", return_value=expected_data) as mock_read_excel:
        result = read_excel_file("fake_path.xlsx")
        assert result == expected_data.where(pd.notna(expected_data), None).to_dict(orient='records')
        mock_read_excel.assert_called_once_with("fake_path.xlsx")

def test_read_excel_file_empty() -> None:
    with pytest.raises(ValueError, match="Путь к файлу не указан"):
        read_excel_file()