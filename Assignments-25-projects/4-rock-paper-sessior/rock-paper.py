print("This is 04-Rock-paper-scissors-Project")

import random

# Emojis for Rock, Paper, Scissors
emojis = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie! 🤝"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win! 🎊"
    else:
        return "You lose! 😢"

# Main game loop
while True:
    # User input
    user_choice = input("\nChoose rock 🪨, paper 📄, or scissors ✂️: ").lower()

    # Validate user input
    if user_choice not in emojis:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    # Computer choice
    computer_choice = random.choice(list(emojis.keys()))

    # Display choices
    print(f"\nYou chose: {emojis[user_choice]}")
    print(f"Computer chose: {emojis[computer_choice]}")

    # Determine and display the result
    result = determine_winner(user_choice, computer_choice)
    print(result)

    # Ask to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! 👋")
        break