def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску в
    формате XXXX XX** **** XXXX"""

    card_mask = str(card_number)[:4] + " " + str(card_number)[4:6] + "** **** " + str(card_number)[-4:]
    return card_mask


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску в
    формате **XXXX"""

    account_mask = "**" + str(account_number)[-4:]
    return account_mask
