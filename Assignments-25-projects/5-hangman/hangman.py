print("This is 05-Hangman-Python-Project")

import random

# List of words for the game
words = ["python", "programming", "hangman", "challenge", "developer", "algorithm"]

# Hangman stages with emojis
hangman_stages = [
    """
    +---+
    |   |
        |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    =========
    """
]

# Function to display the current state of the word
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Main game loop
def hangman_game():
    # Select a random word
    word = random.choice(words)
    guessed_letters = set()
    attempts = 6  # Number of attempts
    hangman_step = 0  # Current stage of hangman

    print("Welcome to Hangman! 🎮")
    print("Guess the word before the hangman is complete. 😊")
    print(display_word(word, guessed_letters))

    while attempts > 0:
        guess = input("\nGuess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter. 🔠")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again! 🔄")
            continue

        guessed_letters.add(guess)

        # Check if the guessed letter is in the word
        if guess in word:
            print(f"Good job! '{guess}' is in the word. 👍")
        else:
            attempts -= 1
            hangman_step += 1
            print(f"Oops! '{guess}' is not in the word. 😢")
            print(f"Attempts left: {attempts}")
            print(hangman_stages[hangman_step])

        # Display the current state of the word
        current_word = display_word(word, guessed_letters)
        print("\nWord: ", current_word)

        # Check if the word has been fully guessed
        if "_" not in current_word:
            print("\nCongratulations! You've guessed the word! 🎉")
            print(f"The word was: {word}")
            break

    # If no attempts are left
    if attempts == 0:
        print("\nGame Over! You've run out of attempts. 😭")
        print(f"The word was: {word}")

# Run the game
hangman_game()