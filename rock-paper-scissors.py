import time

def get_user_choice():
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Choose rock, paper, or scissors: ").lower()
    return user_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'rock':
        return "You win!" if computer_choice == 'scissors' else "Computer wins!"
    elif user_choice == 'paper':
        return "You win!" if computer_choice == 'rock' else "Computer wins!"
    elif user_choice == 'scissors':
        return "You win!" if computer_choice == 'paper' else "Computer wins!"

def play_game():
    print("Let's play Rock-Paper-Scissors!")
    user_choice = get_user_choice()
    
    current_time = int(time.time())  # Get current timestamp
    computer_choices = ['rock', 'paper', 'scissors']
    computer_choice = computer_choices[current_time % 3]
    
    print(f"You chose {user_choice}, and the computer chose {computer_choice}.")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

play_game()

