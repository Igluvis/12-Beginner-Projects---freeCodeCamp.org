# Hangman

import random
from words import words


def play():
    word = list(random.choice(words).lower())
    hangman = ['_' if s.isalpha() else s for s in word]
    used_letters = []
    lives = 6
    while hangman != word and lives > 0:
        guess = input(f"Choose a letter! Lives left: {lives}\nUsed so far: {' '.join(used_letters)}\n{''.join(hangman)}\n")[0]
        if not guess in used_letters:
            used_letters.append(guess)

            if guess in word:
                for i, s in enumerate(word):
                    if guess == s:
                        hangman[i] = guess
            
            else:
                lives -= 1

        print(hangman, word)

    if lives == 0:
        print("You lost! The word was ", word)
    else:    
        print(f"You won. The word was: {''.join(hangman)}")
    
play()