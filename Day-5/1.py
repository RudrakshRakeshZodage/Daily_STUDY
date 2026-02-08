# Chocolate Distribution Problem
# SAMPLE

# Input: arr[] = {7, 3, 2, 4, 9, 12, 56}, m = 3 
# Output: 2 
# Explanation: If we distribute chocolate packets {3, 2, 4}, we will get the minimum difference, that is 2. 

# Python program to solve chocolate distribution
# problem using Sliding Window

def findMinDiff(arr, m):
    n = len(arr)

    # Sort the given packets
    arr.sort()

    minDiff = float('inf')

    for i in range(n - m + 1):

        # calculate difference of current window
        diff = arr[i + m - 1] - arr[i]

        # if current difference is smaller
        # then update the minimum difference
        if diff < minDiff:
            minDiff = diff

    return minDiff

if __name__ == "__main__":
    arr = [7, 3, 2, 4, 9, 12, 56]
    m = 3

    print(findMinDiff(arr, m))