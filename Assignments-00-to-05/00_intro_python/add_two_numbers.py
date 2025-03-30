print("This is 01_add_two_numbers")

def add():
  print("This application for adding two numbers")
  first_number = int(input("Enter your first number here. "))
  second_number = int(input("Enter your second nunber here. "))
  total = int(first_number + second_number)
  print(f'The total sum of {first_number} and {second_number} is {total}')

if __name__ == "__main__":
  add()