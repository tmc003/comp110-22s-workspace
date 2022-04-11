"""Exercise 08."""

__author__ = "730316240"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:   
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]: 
    """Transform a row-oriented table to a column oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], num: int) -> dict[str, list[str]]:
    """Produces a new column-based table with rows equal to the second parameter."""
    result: dict[str, list[str]] = {}
    for column in table:
        new_list: list[str] = []
        i: int = 0
        if len(table[column]) < num:
            return table
        while i < num:
            new_list.append(table[column][i])
            i += 1
        result[column] = new_list
    return result


def select(table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Create a table with a specific desired columns."""
    result: dict[str, list[str]] = {}
    for column in column_names:
        result[column] = table[column]
    return result


def concat(a: dict[str, list[str]], b: dict[str, list[str]]) -> dict[str, list[str]]: 
    """Produce a new table with two columns."""
    result: dict[str, list[str]] = {}
    for item in a:
        result[item] = a[item]
    for item in b:
        if item in result:
            result[item] += b[item]
        else:
            result[item] = b[item]     
    return result


def count(list: list[str]) -> dict[str, int]:
    """Gives each appended column a unique numercial value."""
    result: dict[str, int] = {}
    for item in list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result 


def filter(original: dict[str, list[str]], word: str) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for item in original:
        if item == word:
            result[item] = original[item]
    return result


def helper(original: list[str], filter: list[bool]) -> list[str]:
    result: list[str] = []
    i: int = 0
    while i < len(filter):
        if filter[i]:
            result.append(original[i])
    return result