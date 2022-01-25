"""I'm trying to figure out this assignment 01."""

___author___ = "730316240"

word = input("Enter a 5-character word: ")
word_count = int(len(word))

if word_count == 5:
    character = input("Enter a single character: ")
    character_count = int(len(character))
    print("Searching for", character, "in", word)
    if character_count == 1:
        overlap = word.count(character)
        if overlap == 0:
            print("No instances of", character, "found in", word)
        elif overlap == 1:
            if str(word[0]) == str(character):
                print(character, "found at index 0")
                print(overlap, "instance of", character, "found in", word)
            elif str(word[1]) == str(character):
                print(character, "found at index 1")
                print(overlap, "instance of", character, "found in", word)
            elif str(word[2]) == str(character):
                print(character, "found at index 2")
                print(overlap, "instance of", character, "found in", word)
            elif str(word[3]) == str(character):
                print(character, "found at index 3")
                print(overlap, "instance of", character, "found in", word)
            else:
                print(character, "found at index 4")
                print(overlap, "instance of", character, "found in", word)
        else:
            if word[0] == character:
                print(character, "found at index 0")
            if word[1] == character:
                print(character, "found at index 1")
            if word[2] == character:
                print(character, "found at index 2")
            if word[3] == character:
                print(character, "found at index 3")
            if word[4] == character:
                print(character, "found at index 4") 
            print(overlap, "instances of", character, "found in", word)
    else:
        exit(print("Error: Character must be a single character."))
else:
    exit(print("Error: Word must contain 5 letters."))