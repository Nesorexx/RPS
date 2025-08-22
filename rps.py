import random

def game():
    words = ["Rock", "Paper", "Scissors"]
    user_choice = input("Enter your choice (Rock, Paper or Scissors): ").capitalize()
    while user_choice not in words:
        user_choice = input("Invalid choice. Please enter Rock, Paper or Scissors: ").capitalize()

    computer_choice = random.choice(words)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        print("You win!")
    else:
        print("Computer wins!")

play_again = "yes"
while play_again.lower() == "yes":
    game()
    play_again = input("Do you want to play again? enter(yes/exit): ")
