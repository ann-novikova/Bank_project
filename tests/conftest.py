import pytest

@pytest.fixture
def not_number():
    return 'hello_world_this_is_not_digit'

@pytest.fixture
def less_than_standart_lenght():
    return '11'
