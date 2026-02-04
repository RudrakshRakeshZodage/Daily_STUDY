#Given an integer array nums, find the subarray with the largest sum, and return its sum.


class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]
        curr_sum = nums[0]

        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum

# #
# | Index | Element | Current Sum Calculation | Current Sum | Max Sum | Best Subarray So Far |
# | ----: | ------: | ----------------------- | ----------: | ------: | -------------------- |
# |     0 |      -2 | start with -2           |          -2 |      -2 | [-2]                 |
# |     1 |       1 | max(1, -2 + 1)          |           1 |       1 | [1]                  |
# |     2 |      -3 | max(-3, 1 - 3)          |          -2 |       1 | [1]                  |
# |     3 |       4 | max(4, -2 + 4)          |           4 |       4 | [4]                  |
# |     4 |      -1 | max(-1, 4 - 1)          |           3 |       4 | [4, -1]              |
# |     5 |       2 | max(2, 3 + 2)           |           5 |       5 | [4, -1, 2]           |
# |     6 |       1 | max(1, 5 + 1)           |           6 |       6 | **[4, -1, 2, 1]**    |
# |     7 |      -5 | max(-5, 6 - 5)          |           1 |       6 | [4, -1, 2, 1]        |
# |     8 |       4 | max(4, 1 + 4)           |           5 |       6 | [4, -1, 2, 1]        |
# #