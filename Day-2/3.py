def reverseArray(arr):
    n = len(arr)
    
    for i in range(n // 2):
        temp = arr[i]
        arr[i] = arr[n - i - 1]
        arr[n - i - 1] = temp
    
arr = [1, 4, 3, 2, 6, 5]
reverseArray(arr)  #output: [5, 6, 2, 3, 4, 1]
print("    ", arr) #[5, 6, 2, 3, 4, 1]

#O(n) Time and O(1) Space