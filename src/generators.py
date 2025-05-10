from typing import Any, Generator, Iterator


def filter_by_currency(transaction_list: list[dict[str, Any]], currency: str) -> Iterator[Any]:
    """Фильтрует список транзакций по заданной валюте. Возвращает "Операции по данной валюте отсутствуют",
    если транзакции с указанной валютой не найдены."""

    if any(
        isinstance(transaction.get("operationAmount"), dict)
        and isinstance(transaction.get("operationAmount", {}).get("currency"), dict)
        and transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency.upper()
        for transaction in transaction_list
    ):
        return (
            transaction
            for transaction in transaction_list
            if (
                isinstance(transaction.get("operationAmount"), dict)
                and isinstance(transaction.get("operationAmount", {}).get("currency"), dict)
                and transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency.upper()
            )
        )
    else:
        raise ValueError("Операции по данной валюте отсутствуют")


def transaction_descriptions(transaction_list: list[dict[str, Any]]) -> Generator[Any | None]:
    """Функция, которая возвращает описание транзаций"""
    for item in transaction_list:
        yield item.get("description")


def card_number_generator(start: int, stop: int) -> Generator[str]:
    """ "Функция, которая генерирует номера карт от 1 до 10000000000000000 в шестнадцати-значном
    формате 'ХХХХ ХХХХ ХХХХ ХХХХ'"""

    if 0 < start < 10000000000000000 and start < stop < 10000000000000000:
        for i in range(start, stop + 1):
            card = "0" * (16 - len(str(i))) + str(i)
            yield f"{card[:4]} {card[4:8]} {card[8:12]} {card[12:]}"
    else:
        raise ValueError("Некорректный параметр для генерации")
