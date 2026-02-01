def findMinMax(arr):
    mini = float('inf') 
    maxi = float('-inf')
    
    # Find minimum and maximum
    for num in arr: 
        if num < mini:
            mini = num
        if num > maxi:
            maxi = num
    
    return [mini, maxi]

if __name__ == "__main__":
    arr = [3, 5, 4, 1, 9]
    result = findMinMax(arr)
    print(result[0], result[1])