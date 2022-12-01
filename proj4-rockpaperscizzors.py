import random

def play():
    user = input("Rock(r), Paper(p), Scizzor(s)\nChoose your hand: ".lower())
    ai = random.choice(['r', 'p', 's'])
    print(user, ai)
    if user == ai:
        return 'tie'
    if is_winner(user, ai):
        return 'you won'

    return 'you lost'

def is_winner(player, opponent):
    # r > s; p > r; s > p
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
    return False

print(play())