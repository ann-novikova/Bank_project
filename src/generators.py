from typing import Any, Generator, Union

def filter_by_currency(transaction_list: list[dict[str, Any]], currency: str) -> Union[Generator[dict[str, Any]], str]:

    try:
        if any(
            transaction.get("operationAmount")["currency"].get("code") == currency.upper()
            for transaction in transaction_list
        ):
            return (
                transaction
                for transaction in transaction_list
                if transaction.get("operationAmount")
                and transaction.get("operationAmount").get("currency")
                and transaction.get("operationAmount")["currency"].get("code") == currency.upper()
            )
        else:
            return "Операции по данной валюте отсутствуют"
    except TypeError:
        return "Операции по данной валюте отсутствуют"


def transaction_descriptions(transaction_list: list[dict[str, Any]]) -> Generator[Any | None]:
    return (transaction.get("description") for transaction in transaction_list)


def card_number_generator(start: int, stop: int) -> Generator[str]:
    if 0 < start < 10000000000000000 and start < stop < 10000000000000000:
        for i in range(start, stop + 1):
            card = "0" * (16 - len(str(i))) + str(i)
            yield f'{card[:4]} {card[4:8]} {card[8:12]} {card[12:]}'
    else:
        raise ValueError("Некорректный параметр для генерации")
