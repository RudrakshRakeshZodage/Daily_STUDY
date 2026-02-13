def Pair(arr, target):
    s =set()
    for num in arr:
        
        comp = target - num
        
        if comp in s:
            return True
        
        s.add(num)
    return False


if __name__ == "__main__":
    arr = [1, 5, 7, 8, 34, 3]
    target = 12
    
    if Pair(arr, target):
        print("Yes")
    else:
        print("No")