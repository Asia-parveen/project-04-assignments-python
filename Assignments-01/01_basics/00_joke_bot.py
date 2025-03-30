print("This is 00_joke_bot")


PROMPT = "What do you want? "
JOKE = "Here's a joke for you! Asia was going to the grocery store. A programmer friend tells her: 'Buy a liter of milk, and if they have eggs, get 12.' Asia comes back with 13 liters of milk. The friend asks, 'Why so many?' Asia replies, 'Because they had eggs!' 🤓🥚🥛'"
SORRY = "Sorry I only tell jokes."


def main():
    user_input = input(PROMPT)  
    user_input = user_input.strip().lower()  
    
    if user_input == "joke": 
        print(JOKE)
    else:  
        print(SORRY)


if __name__ == "__main__":
    main()
