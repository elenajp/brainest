"""
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
"""


# def start_ hangman():
#     """A simple hangman game where a letter is taken as the input and no more than 6 wrong guesses are allowed. The output is the complete word"""
# hidden_word = input("Player 1 pick a word: ")
hidden_word = "java"
display_word = "_ " * len(hidden_word)
used_letters = []
guesses = 2

while guesses > 0 and display_word != hidden_word:
    print(display_word)
    print(f"You have {guesses} tries left.")
    guessed_letter = input("Guess a letter: ")
    used_letters.append(guessed_letter)

    if len(guessed_letter) != 1:
        print("Please enter only one letter.")

    if guessed_letter is not guessed_letter.isalpha():
        print("Please enter a valid letter of the alphabet")

    if guessed_letter in used_letters:
        print("You have already guessed that word")

    if guessed_letter in hidden_word:
        for i in range(len(hidden_word)):
            if hidden_word[i] == guessed_letter:
                display_word = display_word[:1] + guessed_letter + hidden_word[i + 1 :]
    else:
        print("Wrong letter, try again.")
        guesses -= 1

    # else:
    #     guesses -= 1
    #     print(f"You have {guesses} tries left.")
    #     print(" ".join(used_letters))
    #     if guesses == 0:
    #         print(f"You have ran out of guesses, you lose :(")
    #         break

# for i in range(len(hidden_word)):
#     if hidden_word[i] == guess:
#         display_word = display_word[:i] + guess + display_word[i + 1 :]
# print(display_word)
# for i in range(len(hidden_word)):
#     if hidden_word[i] == guess:
#         display_word = display_word.replace("_", guess, 1)
# print(display_word)

# print(hidden_word)


# You have already used the letter {guess}, try again
# Congratulations! You won!
# replace() the blanks of the word


# Output
"""
You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
"""
