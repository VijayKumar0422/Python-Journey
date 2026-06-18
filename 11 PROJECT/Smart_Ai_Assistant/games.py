import random


def guess_number():

    secret = random.randint(1, 10)

    while True:

        guess = int(input("Guess Number (1-10) : "))

        if guess == secret:

            print("Correct Answer!")

            break

        elif guess < secret:

            print("Too Low")

        else:

            print("Too High")


def rock_paper_scissors():

    options = ["rock", "paper", "scissors"]

    computer = random.choice(options)

    user = input("rock / paper / scissors : ").lower()

    print("Computer :", computer)

    if user == computer:

        print("Draw")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):

        print("You Win")

    else:

        print("Computer Wins")