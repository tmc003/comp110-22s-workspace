"""Exercise 05 utils functions."""

__author__ = "730316240"


def only_evens(o_list: list[int]) -> list[int]:  # This is the defined function that will create the only evens function
    """This is the function that defines only_evens."""
    i = 0
    for list in o_list:
        if o_list[i] % 2 == 1:
            o_list.pop(i)
        i += 1
    return o_list


def sub(s_list: list[int], x: int, y: int) -> list[int]:  # This is the defined function that will create the sub function
    """This function defines the sub function for the code."""
    n_list: list[int] = list()
    i = x
    while i < y:
        new = s_list[i]
        n_list.append(new)
        i += 1
    return n_list


def concat(list1: list[int], list2: list[int]) -> list[int]:  # This is the defined function that will created the concat function
    sum: list[int] = list()
    list1_total = len(list1)
    list2_total = len(list2)
    i = 0
    while i < list1_total:
        sum.append(list1[i])
        i += 1
    
    i = 0
    while i < list2_total:
        sum.append(list2[i])
        i += 1
    return sum