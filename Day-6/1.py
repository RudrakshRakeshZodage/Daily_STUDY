class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


# Example run
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

obj = Solution()
print(obj.search(nums, target))



# =================================
# Dry Run (Table Explanation)

# | Iteration | left | mid | right | nums[mid] | Decision |
# |----------:|-----:|----:|------:|----------:|----------|
# | 1 | 0 | 3 | 6 | 7 | Left part sorted, target not in left → left = 4 |
# | 2 | 4 | 5 | 6 | 1 | Left part sorted, target in left → right = 4 |
# | 3 | 4 | 4 | 4 | 0 | Target found |


## Time and Space Complexity

# | Type | Complexity |
# |------|------------|
# | Time | O(log n) |
# | Space | O(1) |


