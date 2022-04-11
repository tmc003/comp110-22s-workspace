from __future__ import annotations
from typing import Union


class StrArray:
    items: list[str]

    def __init__(self, items: list[str]):
        """Defines the object being made for the class."""
        self.tems = items

    def __repr__(self) -> str: 
        """Returns a string representation of object."""
        return f"StrArray({self.items})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        """Vectorized concatentation operator."""
        result: list[str] = []
        i: int = 0

        if isinstance(rhs, str):
            for item in self.items: 
                result.append(item + rhs)
        else:
            assert len(self.items) == len(rhs.items)
            while i < len(self.items):
                result.append(self.items[i] + rhs.items[i])
                i += 1
        return StrArray(result)


first: StrArray = StrArray(["Armando", "Brady", "Caleb"])
last: StrArray = StrArray(["Bacott", "Manek", "Love"])
result: StrArray = first + "!!!"
print(result)
print(first + " " + last)