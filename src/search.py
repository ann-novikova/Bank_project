import re
from collections import Counter, defaultdict


def search_string(transactions_list: list[dict], search_string: str) -> list[dict]:
    return [
        transaction
        for transaction in transactions_list
        if re.search(search_string.lower(), transaction["description"].lower())
    ]


def count_by_category(transactions_list: list[dict], category_list: list) -> dict:
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
