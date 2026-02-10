class Solution:
    def maxProduct(self, nums):
        maxProd = nums[0]
        minProd = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            # If current number is negative, swap
            if num < 0:
                maxProd, minProd = minProd, maxProd

            maxProd = max(num, num * maxProd)
            minProd = min(num, num * minProd)

            result = max(result, maxProd)

        return result


# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.