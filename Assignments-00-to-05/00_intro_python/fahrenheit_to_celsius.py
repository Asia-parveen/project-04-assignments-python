print("This is 03_fahrenheit_to_celsius")

def temp():
  print("In this code we are converting fahrenheit to celsius")
  fahrenheit_degree = float(input("Enter your fahrenheit degree. "))
  celsius_degree = (fahrenheit_degree - 32) * 5.0/9.0
  print(f'Tempereture {fahrenheit_degree} F = {celsius_degree} C')

if __name__ == "__main__":
  temp()