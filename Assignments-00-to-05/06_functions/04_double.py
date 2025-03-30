print("This is 04_double")


def double(num: int):
    return num * 2


def main():
    num = int(input("Enter any number: "))
    num_times_2 = double(num)
    print("Double that is", num_times_2)

if __name__ == '__main__':
    main()

