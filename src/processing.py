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

    return sorted(
        list_of_bank_transactions,
        key=lambda transaction: datetime.strptime(str(transaction.get("date"))[:10], "%Y-%m-%d"),
        reverse=reverse,
    )
