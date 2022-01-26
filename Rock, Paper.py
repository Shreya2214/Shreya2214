import random

print("Rock,Paper,Scissors...")

R_P_S = "Rock", "Paper", "Scissors"
computer = random.choice(R_P_S)

player = input("Enter your choice: ").lower().capitalize()

if computer == "Rock" and player == "Rock":
    print("It is a Tie")
elif computer == "Scissors" and player == "Scissors":
    print("It is a Tie")
elif computer == "Paper" and player == "Paper":
    print("It is a Tie")
elif computer == "Rock" and player == "Paper":
    print("Oh no! You Win")
elif computer == "Rock" and player == "Scissors":
    print("I win!")
elif computer == "Paper" and player == "Rock":
    print("I win!")
elif computer == "Paper" and player == "Scissors":
    print("Oh no! You win")
elif computer == "Scissors" and player == "Paper":
    print("I win!")
elif computer == "Scissors" and player == "Rock":
    print("Oh no! You win")
else:
    print("Invalid choice!")



