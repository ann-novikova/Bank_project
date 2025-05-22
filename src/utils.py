import json

def convert_file(path_to_file: str) -> list:
    """Функцию, которая принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях"""

    try:
        with open(path_to_file, 'r', encoding='utf-8') as file:
            transactions_data = json.load(file)

    except FileNotFoundError:
        return []

    if not transactions_data or not isinstance(transactions_data, list):
        return []

    return transactions_data


if __name__ == "__main__":
    print(convert_file(r'C:\Users\user\PycharmProjects\Bank_project\data\operations.json'))

