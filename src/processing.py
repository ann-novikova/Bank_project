from datetime import datetime
from typing import Any, Union


def filter_by_state(list_of_bank_transactions: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    '''Функция  принимает информацию о банковских операциях и фильтрует по указанному статусу
    ('EXECUTED' or 'CANCELED'), по умолчанию сортировка производится по "EXECUTED"'''

    executed_transactions = []

    for transaction in list_of_bank_transactions:
        if transaction.get("state") == state:
            executed_transactions.append(transaction)

    return executed_transactions


def sort_by_date(list_of_bank_transactions: list[dict[str, Any]], reverse: bool = True) \
        -> Union[list[dict[str, Any]], str]:
    """Функция принимает информацию о банковских операциях и сортирует по дате (можно указать порядок
    сортировки - True or False)"""

    def date_format(line: dict[str, Any]) -> Any:
        try:
            date = datetime.strptime(str(line.get("date", 0))[:10], "%Y-%m-%d")
            return date
        except ValueError:
            "Формат даты не соответствует"

    try:
        list_sorted = sorted(
            list_of_bank_transactions, key=lambda transaction: date_format(transaction), reverse=reverse
        )
    except TypeError:
        return "Отсутствует дата"

    return list_sorted
