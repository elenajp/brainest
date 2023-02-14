"""
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
"""

def hangman():
    """A simple hangman game where a letter is taken as the input and no more than 6 wrong guesses are allowed. The output is the complete word"""
    word = "java"
    hidden_word = "_ " * len(word)
    used_letters = []
    guesses = 1

    for letter in word:
        guess = input("Guess a letter: ")
        used_letters.append(guess)
        if guess in word:
            # hidden_word.update()  # This is the next step I am on, update the hidden_word
            print(f"You have {guesses} tries left.")
            print(" ".join(used_letters))
            print(hidden_word)
        else:
            guesses -= 1
            print(f"You have {guesses} tries left.")
            print(" ".join(used_letters))
            if guesses == 0:
                print(f"You have ran out of guesses, you lose :(")
                break
    # print(hidden_word)


hangman()

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
