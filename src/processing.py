from datetime import datetime
from typing import Any


def filter_by_state(list_of_bank_transactions: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    '''Функция  принимает информацию о банковских операциях и фильтрует по указанному статусу
    ('EXECUTED' or 'CANCELED'), по умолчанию сортировка производится по "EXECUTED"'''

    executed_transactions = []

    for transaction in list_of_bank_transactions:
        if transaction.get("state") == state:
            executed_transactions.append(transaction)

    return executed_transactions


def sort_by_date(list_of_bank_transactions: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция принимает информацию о банковских операциях и сортирует по дате (можно указать порядок
    сортировки - True or False)"""

    def date_format(line: dict[str, Any]) -> datetime:
        date_str = line.get("date")
        if not date_str:
            raise ValueError("Отсутствует поле 'date'")
        try:
            return datetime.strptime(date_str[:10], "%Y-%m-%d")
        except ValueError as e:
            raise ValueError(f"Неверный формат даты: {date_str}") from e

    try:
        list_sorted = sorted(list_of_bank_transactions, key=date_format, reverse=reverse)
    except (ValueError, TypeError):
        return [{}]

    return list_sorted
