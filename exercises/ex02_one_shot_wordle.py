"""Exercise 02."""
__author__ = "730316240"
correct = str("python")
index = int(len(correct))
word = str(input(f"What is your { index }-letter guess? "))
guess = int(len(word))


result = ""
i = 0
playing = True
character = False
alternate = 0
w = 0

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"

while guess != index and playing:
    word = input(f"That was not { index } letters! Try again: ")
    guess = len(word)
if guess == index:
    playing = False
    while i < index:
        if word[i] == correct[i]:
            result = str(result + green_box)
            i = i + 1
        else:
             
            while character is not True and i < index:
                if correct[alternate] == word[i]:
                    character = True    
                else:
                    alternate = alternate + 1

            if character is True:
                result = str(result + yellow_box)
                i = i + 1
            else:
                result = str(result + white_box)
                i = i + 1
    
    print(result)

else:
    playing = True


if playing is False:
    if correct == word:
        print("Woo! You got it.")
    else:
        print("Not quite. Try again soon!")
