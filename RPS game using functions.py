import random

def play_rock_paper_scissors():
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    you_win = "you win!"
    you_lose = "you lose!"
    tie = "it's a tie!"
    invalid_choice = "invalid choice!"

    match user_choice:
        case "rock":
            if computer_choice == "scissors":
                print(you_win)
            elif computer_choice == "paper":
                print(you_lose)
            else:
                print(tie)
        case "paper":
            if computer_choice == "rock":
                print(you_win)
            elif computer_choice == "scissors":
                print(you_lose)
            else:
                print(tie)
        case "scissors":
            if computer_choice == "paper":
                print(you_win)
            elif computer_choice == "rock":
                print(you_lose)
            else:
                print(tie)
        case _:
            print(invalid_choice)

play_rock_paper_scissors()
