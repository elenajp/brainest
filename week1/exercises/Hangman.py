hidden_word = input("Player 1 enter a word: ")
display_word = "_ " * len(hidden_word)
used_letters = []
guesses = 6

while guesses > 0 and display_word != hidden_word:

    print(
        " ".join([letter if letter in used_letters else "_" for letter in hidden_word])
    )
    print()

    guessed_letter = input("Player 2 guess a letter: ")

    if "".join(used_letters) == hidden_word:
        print("Congratulations, you guessed the word!")
        break

    if len(guessed_letter) != 1:
        print("Please enter only one letter.")

    if guessed_letter is not guessed_letter.isalpha():
        print("Please enter a valid letter of the alphabet")

    if guessed_letter in used_letters:
        print("You already guessed that letter.")
        continue

    used_letters.append(guessed_letter)

    if guessed_letter in hidden_word:
        print("Good guess!")
    else:
        guesses -= 1
        print("Sorry, that letter is not in the word.")

        if guesses == 0:
            print("Sorry, you ran out of guesses. The word was", hidden_word)
            break
