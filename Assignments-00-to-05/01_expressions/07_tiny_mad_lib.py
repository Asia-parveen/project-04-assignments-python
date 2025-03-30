print("This is 7_tiny_mad_lib")

def mad_lib():
  noun:str = str(input("Enter a noun: "))
  adjective:str = str(input("Enter an adjective here: "))
  verb:str = str(input("Enter a verb here: "))
  print(f"Do you {verb} with your {adjective} {noun}?")



if __name__=="__main__":
  mad_lib()