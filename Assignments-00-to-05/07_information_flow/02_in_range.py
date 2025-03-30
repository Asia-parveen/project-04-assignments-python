print("This is 02_in_range")

def in_range(n, low, high):
   
    if n >= low and n <= high:
        return True

  
    return False



def main():
    n = int(input("Enter any number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))

    if in_range(n, low, high):
        print(f"{n} is between {low} and {high} (inclusive).")
    else:
        print(f"{n} is NOT between {low} and {high}.")

if __name__ == "__main__":
    main()
