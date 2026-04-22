from dice_roll import play_dice
from spc import play_spc

def games():
    while True:
        print("\n===👾MINI GAME MENU👾===")
        print("\n1️⃣  Stone🪨 -Paper📃-Scissors✂️")
        print("2️⃣  Disc Roll🎲")
        print("3️⃣  Exit Game🔚")

        choice = int(input("Enter Your Choice: "))
        
        if choice == 1: play_spc()
        elif choice == 2: play_dice()
        elif choice == 3:
            print("Thanks for playing 🙏")
            break
        else:
            print("Invalid Choice! Try again. 🔄️")

games()