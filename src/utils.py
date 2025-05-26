import json
import logging
import os

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logs_path = os.path.join(root_dir, "logs", "utils.log")

logging.basicConfig(
    filename=logs_path,
    level=logging.INFO,
    encoding="utf-8",
    filemode="w",
    format="%(levelname)s:%(name)s:%(message)s:%(asctime)s",
)
logger = logging.getLogger(__name__)


def convert_file(path_to_file: str) -> list:
    """Функцию, которая принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях"""

    logger.info(f"Начало работы функции {convert_file.__name__}")

    try:
        with open(path_to_file, "r", encoding="utf-8") as file:
            transactions_data = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Ошибка {e}, возвращен пустой список")
        return []

    logger.info("Успешная обработка файла")

    return transactions_data


print(convert_file(r"C:\Users\user\PycharmProjects\Bank_project\data\operations.json"))
