import re
from collections import Counter


def search_string(transactions_list: list[dict], search_string: str) -> list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
     а возвращает список словарей, у которых в описании есть данная строка"""

    return [
        transaction
        for transaction in transactions_list
        if re.search(search_string.lower(), transaction["description"].lower())
    ]


def count_by_category(transactions_list: list[dict], category_list: list) -> dict:
    """Функцию принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории."""

    count_description = dict(
        Counter(
            [
                transaction["description"]
                for transaction in transactions_list
                if transaction["description"] in category_list
            ]
        )
    )
    for category in category_list:
        if category not in count_description:
            count_description[category] = 0

    return count_description
