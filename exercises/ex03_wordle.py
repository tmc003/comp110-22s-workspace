"""Exercise 02."""
__author__ = "730316240"


def contains_char(word: str, character: str) -> bool:
    """Searches indeces of a second input in first input."""
    assert len(character) == 1
    i = 0
    while i < (len(word)):  # search for the indexed character in the word
        if word[i] == character: 
            return True
        else: 
            i += 1
    return False


def emojified(guess: str, word: str) -> str:
    """Returns colored box strings for strings of equal length."""
    assert len(guess) == len(word)
    
    WHITEBOX: str = "\U00002B1C"
    GREENBOX: str = "\U0001F7E9"
    YELLOWBOX: str = "\U0001F7E8"
    i = 0
    output = ""
    while i < len(word):  # start of looking for the indexed character in order to output the codified boxes
        if contains_char(word, guess[i]):
            if word[i] == guess[i]:
                output = (output + GREENBOX)
            else:
                output = (output + YELLOWBOX)
        else:
            output = (output + WHITEBOX)  # an output that results when the character is not in the word
        i = i + 1
    return output


def input_guess(length: int) -> str:
    """Returns a string of the length of the input."""
    guess = input(f"Enter a {length} character word: ")
    while len(guess) != length:
        guess = input(f"That wasn't { length } chars! Try again: ")  # loop to get a gas that is the right length
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    t = 1
    won = False
    word = "codes"
    n = len(word)
    while t < 7 and won is not True:
        print(f" === Turn { t}/6 === ")
        guess = input(f"Enter a {n} character word: ")
        print(emojified(guess, word))
        if guess == word: 
            won = True
        else:
            won = False
            t += 1
    if won is True:
        print(f"You won in {t}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")
    if __name__ == "__main__":
        main()