import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account_card_info, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(account_card_info, expected):
    assert mask_account_card(account_card_info) == expected


@pytest.mark.parametrize(
    "account_card_info, expected",
    [("Мир 1596837868705199", "Мир 1596 83** **** 5199"), ("счет 646861", "Счет **6861")],
)
def test_mask_account_card_not_standart(account_card_info, expected):
    assert mask_account_card(account_card_info) == expected


def test_mask_account_card_empty():
    assert mask_account_card("") == "Пустой номер"


def test_mask_account_card_only_digits():
    assert mask_account_card("7000792289606361") == "7000 79** **** 6361"


def test_mask_account_card_number_not_number(not_number):
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(not_number)
        assert str(exc_info.value) == "Номер должен состоять только из цифр"


@pytest.mark.parametrize(
    "date_info, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2019-07-03T18:35:29.512364", "03.07.2019")]
)
def test_get_date(date_info, expected):
    assert get_date(date_info) == expected


def test_get_date_another_format(not_number):
    with pytest.raises(ValueError):
        get_date(not_number)


def test_get_date_empty():
    with pytest.raises(ValueError):
        get_date("")
