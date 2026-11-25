import random

def get_choices():
    player_choice = input("enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]

    if player_choice not in options:
        return False

    computer_choice = random.choice(options)
    choices ={"player": player_choice, "computer": computer_choice}

    return choices

def check_win(player, computer):
    print(f"\nyou choose: {player}\ncomputer choose: {computer}\n")
    if player == computer:
        return "It's a tie!"

    elif player == "rock" and computer == "paper":
        return "paper covers rock! you lose."
    elif player =="rock" and computer =="scissors":
        return "rock smashes scissor! you win. "

    elif player == "paper" and computer =="rock":
        return "paper covers rock! you win."
    elif player == "paper" and computer == "scissors":
        return "scissors cut paper! you lose."

    elif player == "scissors" and computer == "rock":
        return "rock smashes scissors! you lose"
    elif player == "scissors" and computer == "paper":
        return "scissors cut paper! you win"


while True:
    output = get_choices()
    if output is False:
        print("Invalid choice! Game over.")
        break  #exits loop # return 1 exits entire function
    result = check_win(output["player"], output["computer"])
    print(result)
