import random

# Fungsi untuk menghasilkan pilihan komputer
def generate_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Fungsi untuk menentukan pemenang
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif player_choice == 'rock':
        if computer_choice == 'paper':
            return "Computer wins!"
        else:
            return "Player wins!"
    elif player_choice == 'paper':
        if computer_choice == 'scissors':
            return "Computer wins!"
        else:
            return "Player wins!"
    elif player_choice == 'scissors':
        if computer_choice == 'rock':
            return "Computer wins!"
        else:
            return "Player wins!"

# Fungsi untuk menjalankan game
def play_game():
    print("Welcome to Rock-Paper-Scissors game!")
    print("Enter your choice: rock, paper, or scissors")
    player_choice = input("Your choice: ").lower()
    computer_choice = generate_computer_choice()
    print("Computer choice:", computer_choice)
    result = determine_winner(player_choice, computer_choice)
    print(result)

# Memulai permainan
play_game()

my_list = [1,2,3,4,5]
for item in my_list:
    print(item)