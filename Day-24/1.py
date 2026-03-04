class Solution:
    def maxSubArray(self, nums):
        def divide_and_conquer(left, right):
            # Base case
            if left == right:
                return nums[left]
            
            mid = (left + right) // 2
            
            # Left half
            left_max = divide_and_conquer(left, mid)
            
            # Right half
            right_max = divide_and_conquer(mid + 1, right)
            
            # Cross sum
            left_sum = float('-inf')
            temp = 0
            for i in range(mid, left - 1, -1):
                temp += nums[i]
                left_sum = max(left_sum, temp)
            
            right_sum = float('-inf')
            temp = 0
            for i in range(mid + 1, right + 1):
                temp += nums[i]
                right_sum = max(right_sum, temp)
            
            cross_sum = left_sum + right_sum
            
            return max(left_max, right_max, cross_sum)
        
        return divide_and_conquer(0, len(nums) - 1)