print("This is handout")

import random

NUM_ROUNDS = 5

def get_user_guess():
    """Get user input with validation"""
    guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
    while guess not in ['higher', 'lower']:
        guess = input("Please enter either 'higher' or 'lower': ").strip().lower()
    return guess

def play_round(round_number, score):
    print(f"Round {round_number}")
    user_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)

    print(f"Your number is {user_number}")
    user_guess = get_user_guess()

 
    result = ""
    if user_number == computer_number:
        result = "Aww, that's incorrect. The computer's number was " + str(computer_number)
    elif user_guess == "higher" and user_number > computer_number:
        score += 1
        result = "You were right! The computer's number was " + str(computer_number)
    elif user_guess == "lower" and user_number < computer_number:
        score += 1
        result = "You were right! The computer's number was " + str(computer_number)
    else:
        result = "Aww, that's incorrect. The computer's number was " + str(computer_number)

    print(result)
    print(f"Your score is now {score}\n")
    return score

def evaluate_performance(score, total_rounds):
    print("Thanks for playing!")
    print(f"Your final score is: {score}")
    if score == total_rounds:
        print("Wow! You played perfectly!")
    elif score >= total_rounds // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    score = 0
    for round_number in range(1, NUM_ROUNDS + 1):
        score = play_round(round_number, score)

    evaluate_performance(score, NUM_ROUNDS)

if __name__ == '__main__':
    main()
