import random

def play_dice():
    
    input("Press Enter to Dice the Roll🎲")

    user_roll = random.randint(1,6)
    computer_roll = random.randint(1,6)

    print(f"You Rolled: {user_roll}")
    print(f"Computer Rolled: {computer_roll}")

    if user_roll > computer_roll:
        print("You Win!👑")
    elif user_roll < computer_roll:
        print("Computer Wins!🖥️")
    else:
        print("It's a tie!")
    