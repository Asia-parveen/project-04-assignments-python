print("This is 04_tall_enough_to_ride")

min_height:int = 50
def main():
  user:int = int(input("How tall are you? "))
  if user >= min_height:
    print("you are tall enough to ride")
  else:
    print("you are not tall enough to ride.May be next year you can take this ride.")

if __name__ == "__main__":
  main()