print("This is 03_guess_my_number")

import random  

def main():

    secret_number: int = random.randint(1, 99)
    
    print("I thought of a number between 1 and 99...")
    
 
    guess = int(input("Enter your guess: "))
    
 
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        
        print()  
        guess = int(input("Enter your new guess: ")) 

  
    print("Congratulations! The number was: " + str(secret_number))


if __name__ == '__main__':
    main()
