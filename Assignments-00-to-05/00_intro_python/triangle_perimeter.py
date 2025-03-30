print("This is 05_triangle_perimeter.")

def triangle():
  print("In this code we are solve about perimeter of triangle.")
  side1:float = float(input("Enter your first side no of triangle. "))
  side2:float= float(input("Enter your second side no of triangke. "))
  side3:float = float(input("Enter your third side no of triangle. "))
  total:float = float(side1 + side2 + side3)
  print(f'The perimeter of the triangle is {total}')

if __name__ == "__main__":
  triangle()