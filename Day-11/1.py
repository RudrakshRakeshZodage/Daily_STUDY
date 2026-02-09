# Example 1:

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9


class Solution:
    def trap(self, h):
        l, r = 0, len(h) - 1
        lm, rm = 0, 0
        w = 0

        while l < r:
            if h[l] <= h[r]:
                lm = max(lm, h[l])
                w += lm - h[l]
                l += 1
            else:
                rm = max(rm, h[r])
                w += rm - h[r]
                r -= 1

        return w

