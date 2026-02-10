# Two Pointer Technique - O(n) Time and O(1) Space


def pairInSortedRotated(arr, target):
    n = len(arr)

    # Find the pivot element
    i = 0
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            break
	
    # if whole array is sorted max
    # element will be at last index
    if arr[i] <= arr[i + 1]:
        i += 1
        
    # l is now index of smallest element
    l = (i + 1) % n

    # r is now index of largest element
    r = i

    # Keep moving either l or r till they meet
    while l != r:

        # If we find a pair with sum target, return true
        if arr[l] + arr[r] == target:
            return True

        # If current pair sum is less, move to higher sum
        if arr[l] + arr[r] < target:
            l = (l + 1) % n

        # Move to lower sum side
        else:
            r = (r - 1 + n) % n
    return False
  
if __name__ == "__main__":
    arr = [11, 15, 6, 8, 9, 10]
    target = 16
    if pairInSortedRotated(arr, target):
        print("true")
    else:
        print("false")