print("This is 07_get_list")

def main():
  lst = []
  val = input("Enter a value to add in the list: ")
  while val:
    lst.append(val)
    val = input("Enter a value to add in the list: ")
  print("Here is the list: ", lst)

if __name__ == "__main__":
  main()