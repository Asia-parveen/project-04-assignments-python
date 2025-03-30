import random

print("this is 01_chaotic_counting")
import random  

HAVE_DONE = 0.3  

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return
        print(curr_num)

def done():
 
    if random.random() < HAVE_DONE:
        return True
    return False

def main():
    print("I'm going to count until 10 or until I feel like stopping, which ever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()
