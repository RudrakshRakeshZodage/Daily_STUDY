# Pair Sum in a Sorted and Rotated Array

def pairInSortedRotated(arr, target):  
    s = set()
    for num in arr:
      
        # Calculate the complement that added to
        # num, equals the target
        complement = target - num

        # Check if the complement exists in the set
        if complement in s:
            return True

        # Add the current element to the set
        s.add(num)

    # If no pair is found
    return False
  
if __name__ == "__main__":
    arr = [11, 15, 6, 8, 9, 10]
    target = 16

    if pairInSortedRotated(arr, target):
        print("true")
    else:
        print("false")