import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_correct(list_of_bank_transactions: list[dict[str, str | int]]) -> None:
    # Выход функции со статусом по умолчанию 'EXECUTED'
    assert filter_by_state(list_of_bank_transactions) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

    # Выход функции, если вторым аргументов передано 'CANCELED'
    assert filter_by_state(list_of_bank_transactions, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_empty_state(list_of_bank_transactions_empty_state: list[dict[str, str | int]]) -> None:
    assert filter_by_state(list_of_bank_transactions_empty_state) == []


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "ACTIVE",
            [
                {"id": 41428829, "state": "ACTIVE", "date": "2019-07-03T18:35:29.512364"},
                {"id": 7152306, "state": "ACTIVE", "date": "2019-07-03T18:35:29.512365"},
            ],
        ),
        ("DENIED", [{"id": 939719570, "state": "DENIED", "date": "2018-06-30T02:08:58.425572"}]),
        ("INACTIVE", []),
    ],
)
def test_filter_by_state(
    state: str,
    list_of_bank_transactions_different_state: list[dict[str, str | int]],
    expected: list[dict[str, str | int]],
) -> None:
    assert filter_by_state(list_of_bank_transactions_different_state, state) == expected


def test_sort_by_date(
    list_of_bank_transactions: list[dict[str, str | int]],
    list_of_bank_transactions_sorted_date: list[dict[str, str | int]],
) -> None:
    assert sort_by_date(list_of_bank_transactions) == list_of_bank_transactions_sorted_date


def test_sort_by_date_reverse(
    list_of_bank_transactions: list[dict[str, str | int]],
    list_of_bank_transactions_sorted_date_false: list[dict[str, str | int]],
) -> None:
    assert sort_by_date(list_of_bank_transactions, False) == list_of_bank_transactions_sorted_date_false


def test_sort_by_same_date(list_of_bank_transactions_different_state: list[dict[str, str | int]]) -> None:
    assert sort_by_date(list_of_bank_transactions_different_state) == [
        {"id": 41428829, "state": "ACTIVE", "date": "2019-07-03T18:35:29.512364"},
        {"id": 7152306, "state": "ACTIVE", "date": "2019-07-03T18:35:29.512365"},
        {"id": 939719570, "state": "DENIED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_date_no_date() -> None:
    assert sort_by_date([{"id": 41428829, "state": "ACTIVE"}, {"id": 939719570, "state": "DENIED"}]) == [{}]


def test_sort_date_empty() -> None:
    assert sort_by_date([{}]) == [{}]


def test_sort_by_date_incorrect_format() -> None:
    assert sort_by_date(
        [
            {"id": 41428829, "state": "ACTIVE", "date": "2019/07/03T18:35:29.512364"},
            {"id": 939719570, "state": "DENIED", "date": "2018/06/30T02:08:58.425572"},
        ]
    ) == [{}]
