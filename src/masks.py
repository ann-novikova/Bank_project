def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску в
    формате XXXX XX** **** XXXX"""

    if len(card_number) <= 10:
        raise ValueError("Номер карты должен быть длиннее чем 10 цифр")
    elif not card_number.isdigit():
        raise ValueError("Номер должен состоять только из цифр")
    else:
        card_mask = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
        return card_mask


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску в
    формате **XXXX"""
    if len(account_number) <= 5:
        raise ValueError("Номер счета должен быть длиннее чем 5 цифр")

    if not account_number.isdigit():
        raise ValueError("Номер должен состоять только из цифр")

    account_mask = "**" + account_number[-4:]
    return account_mask
