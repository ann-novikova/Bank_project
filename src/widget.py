from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card_info: str) -> str:
    """Функция для возврата номера счета или карты в формате маски"""

    data_list = account_card_info.split()

    if data_list[0].lower() == "счет":
        for item in data_list:
            if item.isdigit():
                data_list[-1] = get_mask_account(int(item))
        return " ".join(data_list)
    else:
        for item in data_list:
            if item.isdigit():
                data_list[-1] = get_mask_card_number(int(item))
        return " ".join(data_list)


def get_date(date_info: str) -> str:
    """Функция переделывает формат даты в ДД.ММ.ГГГГ"""


    date_list = date_info[:10].split("-")[::-1]
    return ".".join(date_list)
