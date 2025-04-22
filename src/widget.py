from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card_info: str) -> str:
    """Функция для возврата номера счета или карты в формате маски"""

    if not account_card_info:
        return 'Пустой номер'

    data_list = account_card_info.split()

    if data_list[0].title() == "Счет":
        for item in data_list:
            if item.isdigit():
                data_list[-1] = get_mask_account(item)
        return " ".join(data_list).title()
    else:
        if data_list[-1].isdigit():
            data_list[-1] = get_mask_card_number(data_list[-1])
        else:
            raise ValueError('Номер должен состоять только из цифр')
        return " ".join(data_list).title()


def get_date(date_info: str) -> str:
    """Функция переделывает формат даты в ДД.ММ.ГГГГ"""

    date_list = date_info[:10].split("-")[::-1]

    for item in date_list:
        if not item.isdigit():
            raise ValueError('Формат даты "%Y-%m-%dT%H:%M:%S')
    else:
        if 0 < int(date_list[0]) < 32 and 0 < int(date_list[1]) < 13 and 0 < int(date_list[2]) < 2026:
            return ".".join(date_list)



