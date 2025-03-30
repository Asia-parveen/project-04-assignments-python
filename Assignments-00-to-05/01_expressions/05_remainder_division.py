print("This is 05_remainder_division")

def reminder():
  num1:int = int(input("Enter any integer to be divided: "))
  num2:int = int(input("Enter any integer to divide by: "))
  quotient:int = num1 // num2
  remainder:int = num1 % num2
  print(f'The result of these division is {quotient} with the reminder of {remainder}')

if __name__ == "__main__":
  reminder()