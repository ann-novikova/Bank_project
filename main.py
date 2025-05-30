from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.processing import filter_by_state, sort_by_date
from src.utils import convert_file
from src.widget import get_date, mask_account_card
import os
from src.read_files import read_csv_file, read_excel_file

path_to_files = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')


if __name__ == "__main__":
    menu = [
        'JSON-файл',
        'CSV-файл',
        'XLSX-фай'
    ]
    print(f'''Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
''')
    user_input = int(input())
    print(f'Для обработки выбран {menu[user_input-1]}')


    def select_category(user_selection):
        while True:
            if user_selection == 1:
                data = convert_file(os.path.join(path_to_files, 'operations.json'))
                return data
            elif user_selection == 2:
                data = read_csv_file(os.path.join(path_to_files, 'transactions.csv'))
                return data
            elif user_selection == 3:
                data = read_excel_file(os.path.join(path_to_files, 'transactions_excel.xlsx'))
                return data
            else:
                'Введен некорректный пункт меню'

    transactions = select_category(user_input)


    user_choose_category = input('''Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n''').lower()

    filter_by_state(transactions, user_choose_category)



    user_finance_info = "Visa Platinum 7000792289606361"
    print(mask_account_card(user_finance_info))

    date = "2024-03-11T02:26:18.671407"
    print(get_date(date))

    transaction_for_generators = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]

    bank_transactions = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    print(filter_by_state(bank_transactions))

    print(sort_by_date(bank_transactions))

    usd_transactions = filter_by_currency(transaction_for_generators, "USD")
    for _ in range(2):
        print(next(usd_transactions))

    descriptions = transaction_descriptions(transaction_for_generators)
    for _ in range(5):
        print(next(descriptions))

    for card_number in card_number_generator(1, 5):
        print(card_number)

print(convert_file(r"C:\Users\user\PycharmProjects\Bank_project\data\operations.json"))
