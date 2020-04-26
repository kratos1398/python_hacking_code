word = "Tornado"

turns = 5
guesses = ""
while turns != 1:
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            turns = turns -1
    guess = input("Enter a character: ")
    guesses = guess
    if guess == word:
        print("Winner")
        break