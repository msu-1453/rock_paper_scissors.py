import random


def get_choices():
    player_choice = input("enter a choice(rock,paper,scissors):")
    options=["rock","paper","scissors"]
    computer_choice=random.choice(options)
    choices={"player":player_choice,"computer":computer_choice}
    return choices

def check_win(player,computer):
    print(f"you chose {player}, computer chose {computer}")
    
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
        
choices = get_choices()
result = check_win(choices["player"],choices["computer"])     
print(result)   
