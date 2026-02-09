class Solution:
    def findKthLargest(self, a, k):
        k = len(a) - k   # index of kth largest in sorted array

        l, r = 0, len(a) - 1

        while l <= r:
            p = self.part(a, l, r)

            if p == k:
                return a[p]
            elif p < k:
                l = p + 1
            else:
                r = p - 1

    def part(self, a, l, r):
        x = a[r]
        i = l

        for j in range(l, r):
            if a[j] <= x:
                a[i], a[j] = a[j], a[i]
                i += 1

        a[i], a[r] = a[r], a[i]
        return i
    
# Kth Largest Element in an Array (LeetCode 215).
