import random

print("This is 00_guess_my_number.")

def main():
  secret_number = random.randint(1,100)
  print("I thought a number between 1 and 100....")

  guess = int(input("Enter your guess: "))

  while guess != secret_number:
    if guess < secret_number:
      print("Your guess is too low.")
    else:
      print("Your guess is too high.")
    guess = int(input("Enter a guess: "))

  print(f"Congratulation! The number was {secret_number}")


if __name__ == "__main__":
  main()