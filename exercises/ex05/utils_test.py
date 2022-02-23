"""Exercise 05 utils functions."""

__author__ = "730316240"

from utils import concat
from utils import only_evens
from utils import sub


def test_only_evens() -> None:
    new_list: list[int] = only_evens([1, 2, 3, 4, 5, 6])
    total = sum(new_list)
    assert total // 2 == 0


def test_empty_only_evens() -> None:
    test: list[int] = only_evens([])
    assert test == 0


def test_only_odds() -> None:
    new_list: list[int] = only_evens([1, 3, 5, 7, 9])
    i = 0
    while i < len(new_list):
        new_list[i] += 1
        i += 1
    assert sum(new_list) // 2 == 0


def test_concat() -> None:
    new_list: list = concat([], [2])
    assert len(new_list) == 1


def test_concat_length() -> None:
    new_list: list[int] = concat([2, 4, 6, 8], [1, 3, 5, 7])
    assert len(new_list) == 8


def test_concat_sum() -> None:
    new_list: list[int] = concat([100, 115], [23, 26, 28])
    assert sum(new_list) == 292


def test_sub_list() -> None:
    new_list: list[int] = sub([2, 4, 6, 8, 0], 0, 3)
    assert len(new_list) == 2


def test_sub_sum() -> None:
    new_list: list[int] = sub([100, 200, 300, 400, 500, 600, 700, 800], 2, 6)
    assert sum(new_list) == (new_list[2] + new_list[6])


def test_sub_empty() -> None:
    new_list: list[int] = sub([-20, 20, -20, 20, -20, 20, -20, 20], 3, 4)
    assert sum(new_list) == 0


def test_sum_many_items() -> None:
    xs: list[float] = [1.0, 2.0, 3.0]
    assert sum(xs) == 6.0


def test_sum_single_item() -> None:
    xs: list[float] = [110.0]
    assert sum(xs) == 110.0


def test_sum_many_items_again() -> None:
    assert sum([-1.0, 1.0, -2.0, 2.0]) == 0.0