import random

def play_game():
    user = input("Enter your choice, 'r' for rock, 'p' paper, 's' for scissors:\n").lower().strip()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie!"

    if you_win(user, computer):
        return "You won!"

    return "You lost!"

def you_win(player, opponent):
    #This function checks who wins.
    # r > s, s > p, p > r
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") \
        or (player == "p" and opponent == "r"):
        return True

print(play_game())