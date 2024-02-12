# 5) Write a program to implement Rock, Paper, Scissor game between human and computer.
# Make use of random module.

import random

def computers_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def getWinner(human_choice, computer_choice):
    if human_choice == computer_choice:
        return "It's a tie!"
    elif (human_choice == 'rock' and computer_choice == 'scissors') or \
         (human_choice == 'paper' and computer_choice == 'rock') or \
         (human_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Please choose: rock, paper, or scissors.")

    human_choice = input("Your choice: ").lower()
    if human_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose either rock, paper, or scissors.")
        return

    computer_choice = computers_choice()
    print(f"Computer's choice: {computer_choice}")

    result = getWinner(human_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
