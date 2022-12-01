import random

# def computer_guess(n):
#     print(f"Choose a number between 1 and {n}.")
#     run = True
#     while run:
#         guess = random.randint(1, n)
#         decision = input(f"Is your number {guess}?\ny/n: ")
#         match decision:
#             case 'y':
#                 run = False
#             case 'n':
#                 print('Okay. I will try again.')
#             case other:
#                 print('Wrong input!')
    
#     print(f"I guessed that your number was {guess}!")

def computer_guess(n):
    print(f"Choose a number between 1 and {n}.")
    low = 1
    high = n
    answer = ''
    while answer != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        answer = input(f'Is your number {guess}?\nh = higher|l = lower|c = correct\nAnswer: ')
        if answer == 'h':
            low = guess + 1
        elif answer == 'l':
            high = guess - 1
    
    print(f"I guessed that your number was {guess}!")

computer_guess(10)