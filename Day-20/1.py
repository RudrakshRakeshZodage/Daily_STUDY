class Solution:
    def combinationSum(self, c, t):
        r = []

        def bt(i, cur, rem):
            if rem == 0:
                r.append(cur[:])
                return
            if rem < 0:
                return

            for j in range(i, len(c)):
                cur.append(c[j])
                bt(j, cur, rem - c[j])
                cur.pop()

        bt(0, [], t)
        return r

#Question: Given an array of distinct integers candidates and a target integer target, 
# return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.