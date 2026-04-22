import random

def play_spc():
    choices = ["stone", "paper", "scissors"]

    user = input("Enter stone, paper or scissors: ").lower()
    computer = random.choice(choices)

    print(f"Computer Choice: {computer}")

    if user not in choices:
        print("Invalid Choices❌")
        return
    
    if user == computer:
        print("It's a Draw")
    elif (user == "stone" and computer == "scissors") or \
        (user == "paper" and computer == "stone") or \
        (user == "scissors" and computer == "paper"):
        print("You Win!🎊")
    else:
        print("Computer Wins!🤖")