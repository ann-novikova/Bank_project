import pytest

@pytest.fixture
def not_number():
    return 'hello_world_this_is_not_digit'

@pytest.fixture
def less_than_standart_lenght():
    return '11'

@pytest.fixture
def list_of_bank_transactions():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

@pytest.fixture
def list_of_bank_transactions_empty_state():
    return [{'id': 41428829, 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'date': '2018-10-14T08:21:33.419441'}]

@pytest.fixture
def list_of_bank_transactions_different_state():
    return [{'id': 41428829, 'state': 'ACTIVE', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'DENIED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 615064591, 'state': 'ACTIVE', 'date': '2018-10-14T08:21:33.419441'}]