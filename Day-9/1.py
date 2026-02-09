class Solution:
    def maxProfit(self, p):
        mn = float('inf')
        mx = 0

        for x in p:
            if x < mn:
                mn = x
            else:
                mx = max(mx, x - mn)

        return mx


# Note that in your output A should precede B.

# Example:

# Input:[3 1 2 5 3] 

# Output:[3, 4] 

# A = 3, B = 4