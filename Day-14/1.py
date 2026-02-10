class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # If middle element is greater than right,
            # minimum is in right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Minimum is in left half (including mid)
                right = mid

        return nums[left]


#FInd the minimum element in a rotated sorted array.