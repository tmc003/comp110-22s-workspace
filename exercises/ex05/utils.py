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
    num = len(s_list)
    while i < num:
        if s_list[i] == s_list[x]:
            s_list.append(x)
        else:
            if s_list[i] == s_list[y]:
                s_list.append(y)
            else:
                s_list.pop(i)
        i += 1
    return s_list


def concat(list1: list[int], list2: list[int]) -> list: 
    sum: list[int] = list()
    count_s = len(sum)
    count_l1 = int(len(list1))
    count_l2 = int(len(list2))
    total: int = count_l1 + count_l2
    i = 0
    if count_s == 0:
        sum = list1
        while count_s < count_l1:
            sum.append(list1[i])
            i += 1
        
        while count_s < total:
            sum.append(list2[i])
            i += 1
    return sum