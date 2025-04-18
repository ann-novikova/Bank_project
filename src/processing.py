from typing import Any
from datetime import datetime

def filter_by_state(list_of_bank_transactions: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:

    executed_transactions = []

    for transaction in list_of_bank_transactions:
        if transaction.get('state') == state:
            executed_transactions.append(transaction)

    return executed_transactions


def sort_by_date(list_of_bank_transactions: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:

    return sorted(list_of_bank_transactions,
                  key = lambda transaction: datetime.strptime(transaction.get('date')[:10], '%Y-%m-%d'), reverse=reverse)



