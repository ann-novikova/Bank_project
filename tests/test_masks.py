import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize('card_number, expected', [('7000792289606361',
                                                    '7000 79** **** 6361'),
                                                   ('1596837868705199',
                                                   '1596 83** **** 5199'),
                                                   ('0000414228426353',
                                                    '0000 41** **** 6353')])

def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected

@pytest.mark.parametrize('card_number, expected', [('700079228960636164564564',
                                                    '7000 79** **** 4564'),
                                                   ('111111111111',
                                                    '1111 11** **** 1111')])

def test_get_mask_card_number_not_standart_lenght(card_number, expected):
    assert get_mask_card_number(card_number) == expected

def test_get_mask_card_number_less_than_10(less_than_standart_lenght):
    with pytest.raises(ValueError):
        get_mask_card_number(less_than_standart_lenght)

def test_get_mask_card_number_not_number(not_number):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(not_number)
    assert str(exc_info.value) == "Номер должен состоять только из цифр"


@pytest.mark.parametrize('account_number, expected', [('73654108430135874305',
                                                    '**4305'),
                                                   ('15968378687051997665',
                                                   '**7665')])

def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected

@pytest.mark.parametrize('account_number, expected', [('73654108445564532330135874305',
                                                    '**4305'),
                                                   ('11111111',
                                                   '**1111')])

def test_get_mask_account_not_standart_lenght(account_number, expected):
    assert get_mask_account(account_number) == expected

def test_get_mask_account_less_than_5(less_than_standart_lenght):
    with pytest.raises(ValueError):
        get_mask_account(less_than_standart_lenght)

def test_get_mask_account_not_number(not_number):
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(not_number)
        assert str(exc_info.value) == "Номер должен состоять только из цифр"