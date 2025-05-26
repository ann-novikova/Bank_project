import logging
import os

root_dir = (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
logs_path = os.path.join(root_dir, "logs", "masks.log")

logging.basicConfig(
    filename=logs_path,
    level=logging.INFO,
    encoding="utf-8",
    filemode="w",
    format='%(levelname)s:%(name)s:%(message)s:%(asctime)s'
)
logger = logging.getLogger(__name__)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску в
    формате XXXX XX** **** XXXX"""
    logger.info(f"Начало работы функции {get_mask_card_number.__name__}")

    if len(card_number) <= 10:
        logger.error(f"Ошибка {ValueError}: Номер карты должен быть длиннее чем 10 цифр")
        raise ValueError("Номер карты должен быть длиннее чем 10 цифр")
    elif not card_number.isdigit():
        logger.error(f"Ошибка {ValueError}: Номер должен состоять только из цифр")
        raise ValueError("Номер должен состоять только из цифр")
    else:
        card_mask = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
        logger.info("Успешное применение маски к номеру карты")
        return card_mask


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску в
    формате **XXXX"""
    logger.info(f"Начало работы функции {get_mask_account.__name__}")
    if len(account_number) <= 5:
        logger.error(f"Ошибка {ValueError}: Номер счета должен быть длиннее чем 5 цифр")
        raise ValueError("Номер счета должен быть длиннее чем 5 цифр")

    if not account_number.isdigit():
        logger.error(f"Ошибка {ValueError}: Номер должен состоять только из цифр")
        raise ValueError("Номер должен состоять только из цифр")

    account_mask = "**" + account_number[-4:]
    logger.info("Успешное применение маски к номеру счета")
    return account_mask
