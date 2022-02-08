"""Some examples of tender, loving function definitions."""


def love(name: str) -> str:
    """Given a name as a parameter, returns a loving string."""
    return f"I love you {name}"


def spread_love(to: str, n: int) -> str: 
    """Genereates a sring that repeats a loving message n times."""
    love_note = ""
    i = 0
    while i < n:
        from lessons.love_functions import love
        i = i + 1
        love_note += love(to) + "/n"
    return love_note