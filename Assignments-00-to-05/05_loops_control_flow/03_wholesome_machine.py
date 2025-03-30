print("This is 03_wholesome_machine")

correct_affermation = "I am able of doing anything. I put my mantly efforts too."

def main():
  print("Welcome to all the Wholesome Machine")
  while True:
    user_input = input("Please type the following affermation:" + correct_affermation)
    if user_input == correct_affermation:
      print("That\'s right! ")
      break
    else:
      print("ohky but That was not the affermation. Please Try Again!")

if __name__ == "__main__":
  main()