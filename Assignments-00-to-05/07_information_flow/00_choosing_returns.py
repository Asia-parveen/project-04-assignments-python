print("This is 00_choosing_returns")

adult_age: int = 18  # U.S. age

def is_adult(age: int):
    if age >= adult_age:
        return True
    return False

def main():
    age: int = int(input("How old is this person?: "))
    print(is_adult(age))

if __name__ == "__main__":
    main()
