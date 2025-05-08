from typing import Any, Generator, Union

def filter_by_currency(transaction_list: list[dict[str, Any]], currency: str) -> Union[Generator[dict[str, Any]], str]:
    """Фильтрует список транзакций по заданной валюте. Возвращает "Операции по данной валюте отсутствуют",
    если транзакции с указанной валютой не найдены. """

    try:
        if any(
            isinstance(transaction.get("operationAmount"), dict) and
            isinstance(transaction.get("operationAmount", {}).get("currency"), dict) and
            transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency.upper()
            for transaction in transaction_list
        ):
            return (transaction for transaction in transaction_list
                    if (isinstance(transaction.get("operationAmount"), dict) and
                    isinstance(transaction.get("operationAmount", {}).get("currency"), dict) and
                    transaction.get("operationAmount", {}).get("currency", {}).get("code") ==
                    currency.upper()))
        else:
            return "Операции по данной валюте отсутствуют"
    except TypeError:
        return "Операции по данной валюте отсутствуют"


def transaction_descriptions(transaction_list: list[dict[str, Any]]) -> Generator[Any | None]:
    """Функция, которое возвращает описание транзаций"""

    return (transaction.get("description") for transaction in transaction_list)


def card_number_generator(start: int, stop: int) -> Generator[str]:
    """"Функиия, которая генерирует номера карт от 1 до 10000000000000000 в шестнадцати-значном
    формате 'ХХХХ ХХХХ ХХХХ ХХХХ'"""

    if 0 < start < 10000000000000000 and start < stop < 10000000000000000:
        for i in range(start, stop + 1):
            card = "0" * (16 - len(str(i))) + str(i)
            yield f'{card[:4]} {card[4:8]} {card[8:12]} {card[12:]}'
    else:
        raise ValueError("Некорректный параметр для генерации")
