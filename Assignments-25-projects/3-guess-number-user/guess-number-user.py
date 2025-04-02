print("This is 03-Guess-the-Number-Game-Project-user")

import random

def computer_guess_game():
    print("🎉✨ Welcome to the **Guess the Number Game!** 🤖🔢")
    print("🔐 **Think of a secret number between 1 and 10** (Don't tell me! 😉)")

    while True:
        user_secret = input("🤫 **Enter your secret number (1-10) for validation:** ").strip()

        if not user_secret.isdigit():
            print("🚨 **Invalid input! Please enter a number (1-10).** 🔄")
            continue

        user_secret = int(user_secret)

        if user_secret < 1 or user_secret > 10:
            print("⚠️ **Out of range! Please enter a number between 1 and 10.** 🔄")
        else:
            break  # ✅ Valid number entered

    input("\n✅ **Press ENTER when you're ready to start...** 🎮")  # Wait for user

    print("\n🎯 **Let's start the game! I have 3 attempts to guess your number...** 🔎")

    attempts = 0
    max_attempts = 3
    guessed_numbers = set()  # 📝 Track guessed numbers to avoid repetition

    while attempts < max_attempts:
        # 🎯 Ensure computer doesn't repeat the same guess
        while True:
            computer_guess = random.randint(1, 10)
            if computer_guess not in guessed_numbers:
                guessed_numbers.add(computer_guess)
                break

        attempts += 1
        print(f"\n🤖 **Attempt {attempts}/3:** I guess... **{computer_guess}**! 🎯")

        # ✅ User input validation
        while True:
            user_feedback = input("📢 **Is this your number? (Yes/No)** ").strip().lower()
            if user_feedback in ['yes', 'no']:
                break
            print("⚠️ **Invalid response! Please type 'Yes' or 'No'.** 🔄")

        if user_feedback == 'yes':
            print(f"\n🎊 **Hooray! I guessed your number `{computer_guess}` in `{attempts}` attempts!** 🏆🤖")
            if attempts == 1:
                print("🔥 **Wow! First try! I'm a genius!** 🚀😎")
            elif attempts == 2:
                print("😃 **Not bad! Got it in my second attempt!** 👍")
            else:
                print("😅 **That was close! But I finally got it!** 🎯")
            print("👏 **Thanks for playing! Play again soon!** 🎮")
            return  # ✅ End the game

        print("🔄 **Oops! Let me try again...** 🤔")

    # 😞 If computer **fails** after 3 tries
    print(f"\n😞 **Oh no! I couldn't guess your number `{user_secret}` in 3 attempts.** 💔")
    print("🔄 **Better luck next time! Try again? 🎮**")

# 🎮 Start the game
computer_guess_game()