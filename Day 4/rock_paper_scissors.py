import random
while True:
    choices = ["rock", "paper", "scissors"]

    computer_answer = random.choice(choices)

    user_input = input("Enter rock, paper or scissors: ")

    if user_input == computer_answer:
        print("It's a draw")

    elif user_input == "rock" and computer_answer == "scissors":
        print("You won!")

    elif user_input == "paper" and computer_answer == "rock":
        print("You won!")

    elif user_input == "scissors" and computer_answer == "paper":
        print("You won!")

    elif user_input == "rock" and computer_answer == "paper":
        print("You lost!")

    elif user_input == "paper" and computer_answer == "scissors":
        print("You lost!")

    elif user_input == "scissors" and computer_answer == "rock":
        print("You lost!")

    else:
        print("Invalid input!")