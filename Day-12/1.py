class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        # Prefix product
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Suffix product
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer


# 🧾 Input Array
# nums = [1, 2, 3, 4]

# 🟢 PREFIX (LEFT PRODUCT) TABLE
# i	nums[i]	prefix (before)	answer[i]	prefix (after)
# 0	1	1	1	1 × 1 = 1
# 1	2	1	1	1 × 2 = 2
# 2	3	2	2	2 × 3 = 6
# 3	4	6	6	6 × 4 = 24

# After prefix loop:

# answer = [1, 1, 2, 6]

# 🔵 SUFFIX (RIGHT PRODUCT) TABLE
# i	nums[i]	suffix (before)	answer[i] = answer[i] × suffix	suffix (after)
# 3	4	1	6 × 1 = 6	1 × 4 = 4
# 2	3	4	2 × 4 = 8	4 × 3 = 12
# 1	2	12	1 × 12 = 12	12 × 2 = 24
# 0	1	24	1 × 24 = 24	24 × 1 = 24
# ✅ FINAL ANSWER
# [24, 12, 8, 6]