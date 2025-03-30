print("This is 08_print_multiple")

def print_multiple(message, repeats):
    for _ in range(repeats):
        print(message)

def main():
    message = input("Please type any message here: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)

if __name__ == '__main__':
    main()
