import os
import random

def main():
    # game score initialization
    score = 0

    # game loop
    while True:

        # options initialisation
        choices = ["r", "p", "s"]
        choices_dict = {
            "r": "rock",
            "p": "paper",
            "s": "scissors"
        }

        # display some information
        os.system('cls||clear')
        print("Rock Paper Scissors")
        print()
        print("--------------------------------------------------")
        print()
        print("Type: r - rock, p - paper, s - scissors, x - exit")
        print()
        print("---------")
        print("Score:", score)
        print("---------")
        print()

        # ask for user choice
        user_choice = input("Your Pick: ")

        # validate if user choice is in list
        if user_choice in choices:
            # generate random computer choice
            computer_choice = random.choice(choices)

            # display user and computer choices
            print()
            print("Your Pick:", choices_dict[user_choice])
            print("Computer's Pick:", choices_dict[computer_choice])
            print()

            # get who wins
            winner = is_winner(user_choice, computer_choice, score)
            print(winner[0])

            # change value of score depending on outcome
            if len(winner) > 1:
                score = winner[1]
            
            # redisplay score
            print()
            print("---------")
            print("Score:", score)
            print("---------")
            print()

            # do you want to replay?
            print("Do you want to play another round? y - yes, n - no")
            repeat = input("Your choice: ")
            print()

            # if yes, clear the terminal and repeat the game loop, 
            # else exit by breaking out of loop
            if repeat == "y":
                os.system('cls||clear')
                continue
            elif repeat == "n":
                print("Thank you for playing!")
                print()
                break
        elif user_choice == "x":
            break
        else:
            print("Invalid Pick!")
            print()


def is_winner(user, computer, score):
    # handle winning and losing logic 
    # and increment the score depending on which happens
    if user == "r" and computer == "s" or user == "p" and computer == "r" \
        or user == "s" and computer == "p":
        score += 1
        return ("You win!", score)
    elif user == computer:
        return ("It's a tie!",)
    else:
        if score > 0:
            score -= 1
        return ("You lost!", score)


main()