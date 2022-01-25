"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730316240"

word = str(input("Enter a 5-character word: "))

count = int(len(word))  

if count == 5:
    character = str(input("Enter a single character: "))
    print("Searching for", character, "in", word)
    single = int(len(character))
    if single == 1:
        appearances = int(word.count(character))
        if appearances == 0:
            print("No instances of", character, "found in", word)
            exit()
        elif appearances == 1:
            if word[0] == character:
                print(character, "found at index 1")
                print("1 instance of", character, "found in", word)
            if word[1] == character:
                print(character, "found at index 2")
                print("1 instances of", character, "found")
            if word[2] == character:
                print(character, "found at index 3")
                print("1 instance of", character, "found in", word)
            if word[3] == character:
                print(character, "found at index 4")
                print("1 instance of", character, "found in", word)
            if word[4] == character:
                print(character, "found at index 5")
                print("1 instance of", character, "found in", word)
        else:
            if appearances > 1:
                if word[0] == character:
                    print(character, "found at index 1")
                if word[1] == character:
                    print(character, "found at index 2")
                if word[2] == character:
                    print(character, "found at index 3")
                if word[3] == character:
                    print(character, "found at index 4")
                if word[4] == character:
                    print(character, "found at index 5")
                if appearances > 1:
                    print(appearances, "instances of", character, "found in", word)
    else:
        print("Character must be a single character.")
        exit()
else:
    print("Error: Word must contain 5 characters")
    exit()
