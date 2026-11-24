wordlist = [
    "hangman",
    "llama",
    "python"
]

import random

bad_guesses = []
word = wordlist[random.randint(0, len(wordlist) - 1)]
board = list("_" * len(word))
max_wrong = 6

while len(bad_guesses) < max_wrong and "_" in board:
    print("Welcome To Hangman\n")
    print(board)

    guess = input("Guess A Letter: ")

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        input("Press [enter] to continue. ")
        continue

    guess = guess.lower()

    if guess in bad_guesses or guess in board:
        print("You already guessed that")
        input("Press [enter] To Continue")
        continue

    is_found = False

    for i, letter in enumerate(word, start=0):
        if letter == guess:
            board[i] = word[i]
            is_found = True

    if not is_found:
        bad_guesses.append(guess)
        print(guess, "Is Not In The Word")

    if "_" not in board:
        print("YOU WON")
    elif len(bad_guesses) == max_wrong:
        print("YOU LOST")
        print("The word was:", word)

    print("Wrong guesses:", bad_guesses)