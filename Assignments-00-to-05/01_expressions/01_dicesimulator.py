import random

print("This is 01_dicesimulator")

def roll_dice():
  die1:int = random.randint(1,6)
  die2:int = random.randint(1,6)
  total:int = die1 + die2
  print(f'Total of two dies is: {total}')

def main():
  die1:int = 10
  print("die1 in main() start as: " + str(die1))
  roll_dice()
  roll_dice()
  roll_dice()
  print("die1 in main() is: " + str(die1))

if __name__ == "__main__":
  main()