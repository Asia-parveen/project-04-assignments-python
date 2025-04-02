print("This is 02-Guess-the-Number-Game-computer")

import random

def guess_the_number():
    print("🎉✨ Welcome to the Ultimate Guess the Number Game! 🔢🎯")
    print("🤖 I have selected a **secret number** between **1 and 10**. Can you guess it? 🕵️‍♂️🔎")
    print("🎮 Let's play! Type your guess below. 👇")

    secret_number = random.randint(1, 10)  # 🔢 Computer chooses a random number
    attempts = 0  # 🔄 Keep track of user attempts

    while True:
        try:
            user_guess = int(input("🔢 Enter your guess (1-10): "))  # 🎯 Take user input

            if user_guess < 1 or user_guess > 10:
                print("⚠️ Invalid Choice! Please enter a number **between 1 and 10**. 🔄")
                continue  # 🔄 Restart loop if number is out of range

            attempts += 1  # 🔢 Increment attempt count

            if user_guess < secret_number:
                print("🔽 Oops! Too **low**! Try a bigger number. 🚀")
            elif user_guess > secret_number:
                print("🔼 Oops! Too **high**! Try a smaller number. 🎯")
            else:
                print(f"🎊🎉 **Hooray! You guessed the correct number `{secret_number}` in `{attempts}` attempts!** 🏆🥇")
                print("👏 Thanks for playing! 🎮 Play again soon! 🔄")
                break  # ✅ Exit loop if the guess is correct

        except ValueError:
            print("⚠️ **Oops! Invalid input.** Please enter a valid number between 1 and 10. 🔁")  # 🚨 Handle non-integer input

# 🎮 Start the game
guess_the_number()