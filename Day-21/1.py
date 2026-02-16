class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])
                path.pop()

        backtrack(0, [], 0)
        return res

# LOGIC :- 
# Question: Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target. Each number in candidates may only be used once in the combination. The solution set must not contain duplicate combinations.

# Sort → group duplicates

# Backtrack → try all combinations

# Skip duplicates

# if i > start and candidates[i] == candidates[i-1]:
#     continue


# Use once → call backtrack(i + 1, ...)

# 👉 Core idea: DFS + no reuse + skip same-level duplicates 🔥