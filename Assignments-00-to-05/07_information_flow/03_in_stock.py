print("This is 03_in_stock")


def num_in_stock(fruit):
 
    if fruit == 'banana':
        return 20
    if fruit == 'apple':
        return 40
    if fruit == 'mango':
        return 100
    else:
    
        return 0


def main():
 
    fruit: str = input("Enter a fruit: ")
    

    stock = num_in_stock(fruit)
    
  
    if stock == 0:
        print("This fruit is not in stock.")
    else:
      
        print("This fruit is in stock! Here is how many:")
        print(stock)


if __name__ == '__main__':
    main()
