import pandas as pd


def read_csv_file(path_csv_to_file: str | None = None) -> list[dict]:
    """Функция для считывания финансовых операций из CSV принимает
    путь к файлу CSV в качестве аргумента."""

    if not path_csv_to_file:
        raise ValueError("Путь к файлу не указан")

    with open(path_csv_to_file, "r", encoding="utf-8") as f:
        data = pd.read_csv(f, delimiter=";")
        data = data.where(pd.notna(data), None)
        csv_result = data.to_dict(orient="records")

    return csv_result


def read_excel_file(path_excel_to_file: str | None = None) -> list[dict]:
    """Функция для считывания финансовых операций из Excel
    принимает путь к файлу Excel в качестве аргумента."""

    if not path_excel_to_file:
        raise ValueError("Путь к файлу не указан")

    data = pd.read_excel(path_excel_to_file)
    data = data.where(pd.notna(data), None)
    excel_result = data.to_dict(orient="records")

    return excel_result
