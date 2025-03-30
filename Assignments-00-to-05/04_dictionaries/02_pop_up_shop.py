print("This is 02_pop_up_shop")

def calculate_total_cost():
  fruits_price = {
      "banana":5.0,
      "orange":10.0,
      "kiwi":8.0,
      "jackfruit":12.0,
      "apple":6.0,
      "mango":10.0
    
  }

  total_cost = 0

  for fruit,price in fruits_price.items():
    while True:
      try:
        quantity = int(input(f'How many {fruit} do you want?: '))
        if quantity < 0:
          print("Invalid input. Please enter a non-negative number here.")
          continue
        total_cost += price * quantity
        break
      except ValueError:
        print("Invalid input. Please enter a valid number here.")

    print(f"\n Your total cost is: ${total_cost:.2f}")

if __name__ == "__main__":
  calculate_total_cost()