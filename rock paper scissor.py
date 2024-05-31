import random
def get_choices():
        player_choice = input("enter a choice i.e. rock, paper or scissor")
        options = ["rock", "paper", "scissor"]
        computer_choice = random.choice(options)
        choices = {"player": player_choice , "computer": computer_choice}
        return choices
        
def check_win(player, computer):
    print(f"you chose {player} and computer chose {computer}")
    if player == computer:
        return "its a tie!"
    elif player == "rock":
        if computer == "scissor":
            return "you win"
        else:
            return "you lose"
    elif player ==" paper":
        if computer == "rock":
            return "you win"
        else:
            return "you lose"
    elif player == "scissor":
        if computer == "paper":
            return "you win"
        else:
            return "you lose"
            
            
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print (result)