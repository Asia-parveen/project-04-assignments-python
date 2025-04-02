print("This is 06-Countdown-Timer-Python-Project")

import time
from tqdm import tqdm  # For progress bar

# Function to display the countdown timer
def countdown_timer(seconds):
    print("\nStarting the countdown timer... 🚀")
    for sec in tqdm(range(seconds), desc="⏳ Counting Down", unit="s"):
        time.sleep(1)

    # When the timer ends
    print("\n⏰ Time's up! 🎉")

# Function to validate user input
def get_time_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative number. 🔢")
                continue
            return value
        except ValueError:
            print("Invalid input! Please enter a number only. 🔢")

# Main function to run the countdown timer
def main():
    print("Welcome to the Countdown Timer! 🎮")

    # Get the countdown time from the user
    hours = get_time_input("Enter hours: ")
    minutes = get_time_input("Enter minutes: ")
    seconds = get_time_input("Enter seconds: ")

    # Convert everything into seconds
    total_seconds = hours * 3600 + minutes * 60 + seconds

    # Check if the total time is greater than 0
    if total_seconds <= 0:
        print("Please enter a valid time greater than 0. ⏱️")
        return

    # Start the countdown timer
    countdown_timer(total_seconds)

# Run the program
if __name__ == "__main__":
    main()