import random

number = random.randint(1, 99)
game = True
guessed_numbers = []

while game:
    guess = int(input("Guess a number between 0 and 100: "))
    if guess == number:
        game = False
    else:
        guessed_numbers.append(str(guess))
        print(f"Wrong number. Our number is {'higher' if guess < number else 'lower'}. Guessed numbers so far: {', '.join(guessed_numbers)}")

print(f"Nice. {guess} was the correct number.")