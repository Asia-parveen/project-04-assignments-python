print("This is 01_double_it")

def main():
    # User se number lena
    user_input = int(input("Enter a number: "))
    
    # Us value ko current value banate hain
    curr_value = user_input

    # Jab tak current value 100 se choti hai, double karte raho
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value)

# Program start karna
if __name__ == "__main__":
    main()
