"""Exercise 01."""
__author__ = "730316240"

word = str(input("What is your guess? "))
character = str(input("What is your character"))
result = bool
i = 0

while i < (len(word)):
    if word[i] == character: 
        result = True
    else: 
        i += 1
print(result)