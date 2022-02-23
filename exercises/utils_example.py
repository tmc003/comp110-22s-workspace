"""Exercise 05 utils functions."""

__author__ = "730316240"


def only_evens(o_list: list[int]) -> list:
    """This is the function that defines only_evens."""
    num = len(o_list)
    i = 0
    while i < num:
        if o_list[i] // 2 == 0:
            o_list.append(o_list[i])
        else:
            o_list.pop(o_list[i])     
        i += 1
    return o_list


def sub(s_list: list[int], x: int, y: int) -> list:
    """This function defines the sub function for the code."""
    i = 0
    for s in s_list:
        if s_list[x]:
            s_list.append(x)
        else:
            if s_list[y]:
                s_list.append(y)
            else:
                s_list.pop(i)
        i += 1
    return s_list


def concat(list1: list[int], list2: list[int]) -> list: 
    sum: list[int] = list()
    list1_total = len(list1)
    total = list1_total + len(list2)
    i = 0
    while i < list1_total:
        sum.append(list1[i])
        i += 1
    
    while i < total:
        sum.append(list2[i])
        i += 1
    return sum