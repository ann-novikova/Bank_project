from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.processing import filter_by_state, sort_by_date
from src.utils import convert_file
import os
from src.widget import get_date, mask_account_card
from src.read_files import read_csv_file, read_excel_file
from src.search import search_string

path_to_files = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')


if __name__ == "__main__":
    menu = [
        'JSON-файл',
        'CSV-файл',
        'XLSX-фай'
    ]

    def select_category() -> list[dict]:
        while True:
            print(f'''Привет! Добро пожаловать в программу работы с банковскими транзакциями. 
            Выберите необходимый пункт меню:
            1. Получить информацию о транзакциях из JSON-файла
            2. Получить информацию о транзакциях из CSV-файла
            3. Получить информацию о транзакциях из XLSX-файла\n
            ''')
            user_input = int(input())
            print(f'Для обработки выбран {menu[user_input - 1]}')
            if user_input == 1:
                data = convert_file(os.path.join(path_to_files, 'operations.json'))
                return data
            elif user_input == 2:
                data = read_csv_file(os.path.join(path_to_files, 'transactions.csv'))
                return data
            elif user_input == 3:
                data = read_excel_file(os.path.join(path_to_files, 'transactions_excel.xlsx'))
                return data
            else:
                print('Введен некорректный пункт меню')

    transactions = select_category()
    print(transactions)

    def choose_category_filter(transaction: list[dict]) -> list[dict] | None:
        available_status = ['executed', 'canceled', 'pending']
        while True:
            user_choose_category = input('''Введите статус, по которому необходимо выполнить фильтрацию. 
            Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n''').lower()
            if user_choose_category in available_status:
                return filter_by_state(transaction, user_choose_category.upper())
            else:
                print(f'Статус операции {user_choose_category} недоступен')
                continue

    filtered_transaction = choose_category_filter(transactions)
    print(filtered_transaction)

    def choose_params_for_date(transaction: list[dict]) -> list[dict] | None:
        while True:
            sort_input = input('Отсортировать операции по дате? Да/Нет\n').lower()
            if sort_input == 'нет':
                return transaction
            elif sort_input == 'да':
                while True:
                    order = input('Отсортировать по возрастанию или по убыванию? в/у\n').lower()
                    if order == 'в':
                        return sort_by_date(transaction, False)
                    elif order == 'у':
                        return sort_by_date(transaction, True)
                    else:
                        print('Введите пожалуйста корректное значение')
                        continue
            else:
                print('Введите пожалуйста корректное значение')

    transactions_sorted = choose_params_for_date(filtered_transaction)

    def choose_rub(transactions_list_sorted: list[dict]) -> list[dict]:
        while True:
            user_rub_input = input('Выводить только рублевые транзакции? Да/Нет\n').lower()
            if user_rub_input == 'нет':
                return transactions_list_sorted
            elif user_rub_input == 'да':
                try:
                    return list(filter_by_currency(transactions_list_sorted, 'RUB'))
                except ValueError:
                    print('Операции по данной валюте отсутствуют')
            else:
                print('Введите пожалуйста корректное значение')


    transactions_rub_sorted = choose_rub(transactions_sorted)

    def choose_search(operations_list) -> list[dict]:
        while True:
            user_search_input = (
                input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n').lower())
            if user_search_input == 'нет':
                return operations_list
            elif user_search_input == 'да':
                user_word = input('Введите пожалуйста слово в описании операции для поиска\n').lower()
                return search_string(operations_list, user_word)
            else:
                print('Введите пожалуйста корректное значение')

    final_result = choose_search(transactions_rub_sorted)

    print('Программа: Распечатываю итоговый список транзакций...')
    print(f'Всего банковских операций в выборке: {len(final_result)}')

    for transaction in final_result:
        date = get_date(transaction['date'])
        amount = transaction["amount"] if "amount" in transaction else transaction["operationAmount"]["amount"]
        from_transaction = mask_account_card(transaction.get("from"))
        to_transaction = mask_account_card(transaction.get("to"))
        description = transaction["description"]
        currency_code = (
            transaction["currency_code"]
            if "currency_code" in transaction
            else transaction["operationAmount"]["currency"]["name"]
        )
        print(f'{date} {description}\n{from_transaction} -> {to_transaction}\nСумма: {amount} {currency_code}\n\n')
