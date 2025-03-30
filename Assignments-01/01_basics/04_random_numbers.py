print("This is 04_random_numbers")

import random

n_number: int = 10
min_value: int = 1
max_value: int = 100

def main():

    for _ in range(n_number):
        value = random.randint(min_value,max_value)  
        print(value, end=' ')  

if __name__ == '__main__':
    main()
