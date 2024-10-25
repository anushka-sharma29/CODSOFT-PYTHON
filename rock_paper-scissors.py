# Task-4 (Rock-Paper-Scissors Game)

import random

def get_player_choice():
    player_choice = input("Enter a choice (rock, paper, scissors): ").lower()
    while player_choice not in ["rock", "paper", "scissors"]:
        player_choice = input("Invalid entry. Choose a valid option: rock, paper, scissors- ").lower()
    return player_choice

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "System wins!"

def play_game():
    print("Welcome our Rock, Paper and Scissors game!!")
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print(f"\nYou chose {player_choice}, computer chose {computer_choice}.")
        print(determine_winner(player_choice, computer_choice))
        
        play_again = input("\nDo you want to play again?: ").lower()
        if play_again != "yes":
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
