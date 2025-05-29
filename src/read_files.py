import pandas as pd

def read_csv_file(path_csv_to_file: str) -> list[dict]:
    """Функция для считывания финансовых операций из CSV принимает
    путь к файлу CSV в качестве аргумента."""

    if path_csv_to_file:

        with open(path_csv_to_file, 'r', encoding='utf-8') as f:
            data = pd.read_csv(path_csv_to_file, delimiter=';')
            csv_result = data.to_dict(orient='records')

        return csv_result

    else:
        raise ValueError("Путь к файлу не указан")


def read_excel_file(path_excel_to_file: str) -> list[dict]:
    """Функция для считывания финансовых операций из Excel
    принимает путь к файлу Excel в качестве аргумента."""

    if path_excel_to_file:

        with open(path_excel_to_file, 'r', encoding='utf-8') as f:
            data = pd.read_excel(path_excel_to_file)
            excel_result = data.to_dict(orient='records')

        return excel_result

    else:
        raise ValueError("Путь к файлу не указан")
