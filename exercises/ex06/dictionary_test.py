"""This will test the functions made in utils."""

__author__ = "730316240"

from dictionary import count
from dictionary import favorite_color
from dictionary import invert


def test_count() -> None:  # This test will make sure that all the components of the list are even
    new_list: list[int] = only_evens([1, 2, 3, 4, 5, 6])
    total = sum(new_list)
    assert total % 2 == 0


def test_empty_only_evens() -> None:  # This test will make sure that only_evens is empty
    test: list[int] = only_evens([])
    assert len(test) == 0


def test_only_odds() -> None:  # This test will make only even function compnents odd
    new_list: list[int] = only_evens([1, 3, 5, 7, 9])
    i = 0
    while i < len(new_list):
        new_list[i] += 1
        i += 1
    assert sum(new_list) % 2 == 0


def test_concat() -> None:  # This test will make sure that the combined list only has one element
    new_list: list[int] = concat([], [2])
    assert len(new_list) == 1


def test_concat_length() -> None:  # This tst will the total length of the combined list
    new_list: list[int] = concat([2, 4, 6, 8], [1, 3, 5, 7])
    assert len(new_list) == 8


def test_concat_sum() -> None:  # This test will find the sum of a combined list
    new_list: list[int] = concat([100, 115], [23, 26, 28])
    assert sum(new_list) == 292


def test_sub_list() -> None:  # This function will make sure that there are only 2 elements in a list
    the_list = [2, 4, 6, 8, 0]
    new_list: list[int] = sub(the_list, 0, 3)
    assert len(new_list) == 3


def test_sub_sum() -> None:  # This function will find the sum of the two elements of the sub list
    the_list = [100, 200, 300, 400, 500, 600, 700, 800]
    new_list: list[int] = sub(the_list, 0, 2)
    assert sum(new_list) == the_list[2]


def test_sub_empty() -> None:  # This function will make sure that the sub list is empty
    the_list = [-20, 20, -20, 20, -20, 20, -20, 20]
    new_list: list[int] = sub(the_list, 3, 5)
    assert sum(new_list) == 0