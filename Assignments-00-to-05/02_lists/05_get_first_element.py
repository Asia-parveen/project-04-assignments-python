print("This is 05_get_first_element")

def get_first_element(lst):
  print(lst[0])

def get_lst():
  lst = []
  element:str = input("write any element you want to add in the list: ")
  while element != "":
    lst.append(element)
    return lst

def main():
  lst = get_lst()
  get_first_element(lst)

if __name__ == "__main__":
  main()