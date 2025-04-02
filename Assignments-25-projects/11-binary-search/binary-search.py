


def binary_search(arr, target):

    start = 0
    end = len(arr) - 1

    while start <= end:
    
        mid = (start + end) // 2
        
     
        if arr[mid] == target:
            return mid  # Target found, return the index
        
      
        elif arr[mid] < target:
            start = mid + 1
        
      
        else:
            end = mid - 1
    
    return -1  


def search_element():
  
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
    
  
    target = int(input("Enter the element you want to search for: "))
    

    result = binary_search(arr, target)
    
   
    if result != -1:
        print(f"Element {target} is present at index {result}.")
    else:
        print(f"Element {target} is not found in the array.")


if __name__ == "__main__":
    search_element()
