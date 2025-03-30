
print("This is 00_averages")

def average(a: float, b: float):
    
    sum = a + b
    return sum / 2

def main():
    avg_1 = average(0, 10)
    avg_2 = average(8, 10)
    
    result = average(avg_1, avg_2)
    print("avg_1", avg_1)
    print("avg_2", avg_2)
    print("result", result)
    



if __name__ == '__main__':
    main()