import random

def play_rock_paper_scissors():
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    match user_choice:
        case "rock":
            if computer_choice == "scissors":
                print("You win!")
            elif computer_choice == "paper":
                print("You lose!")
            else:
                print("It's a tie!")
        case "paper":
            if computer_choice == "rock":
                print("You win!")
            elif computer_choice == "scissors":
                print("You lose!")
            else:
                print("It's a tie!")
        case "scissors":
            if computer_choice == "paper":
                print("You win!")
            elif computer_choice == "rock":
                print("You lose!")
            else:
                print("It's a tie!")
        case _:
            print("Invalid choice!")

play_rock_paper_scissors()
