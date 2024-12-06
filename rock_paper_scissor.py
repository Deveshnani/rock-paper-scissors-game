#simple game 
import random

#creating a dict 
youDict = {"r": 1, "p": 2, "s": 3}
reverseDict = {1: "Rock", 2: "Paper", 3: "Scissors"}

#taking inputs from user and generating a random num
computer = random.choice([1, 2, 3])
youstr = input("Enter your choice (r for Rock, p for Paper, s for Scissors): ").lower()


if youstr not in youDict:
    print("Invalid choice! Please enter 'r', 'p', or 's'.")
else:
    you = youDict[youstr]

    print(f"You chose {reverseDict[you]}")
    print(f"Computer chose {reverseDict[computer]}")

    if computer == you:
        print("It's a draw!")
    elif (you == 1 and computer == 3) or (you == 2 and computer == 1) or (you == 3 and computer == 2):
        print("You win!")
    else:
        print("You lose!")
