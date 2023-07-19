import random


def get_choices():
    player_choice = input("Enter a choice (rock, paper. scissors : ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


choice = get_choices()


def check_win(player, computer):
    print(f"You choose {player} computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper Cover Rocks! You win!"
        else:
            return "Scissors cuts paper! You lose."
    elif player == "Scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose!"


check_win("Player", "Ball")
