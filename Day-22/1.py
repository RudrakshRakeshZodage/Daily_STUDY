class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1
# Question: Given an unsorted integer array nums, return the smallest missing positive integer.
#Real-life application: Finding the first missing positive integer can be useful in scenarios like assigning unique IDs, 
# managing inventory, or scheduling tasks where you need to identify the next available slot.