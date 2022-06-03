import random

while True:
    choices = ["R", "P", "S"]

    CPU = random.choice(choices)
    player = None
    while player not in choices:
        player = input("R, P or S?: ").lower()

    if player == CPU:
        print("CPU: ", CPU)
        print("you: ", player)
        print("It's a Tie!!")
    elif player == "R":
        if CPU == "P":
            print("CPU: ", CPU)
            print("you: ", player)
            print("You lose!!")
        if CPU == "S":
            print("CPU: ", CPU)
            print("you: ", player)
            print("You win!!")
    elif player == "P":
        if CPU == "S":
            print("CPU: ", CPU)
            print("you: ", player)
            print("You lose!!")
        if CPU == "R":
            print("CPU: ", CPU)
            print("you: ", player)
            print("You win!!")
    elif player == "S":
        if CPU == "R":
            print("CPU: ", CPU)
            print("you: ", player)
            print("You lose!!")
        if CPU == "P":
            print("CPU: ", CPU)
            print("you: ", player)
            print("You win!!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break
print("Bye")

