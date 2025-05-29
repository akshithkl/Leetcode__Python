class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur[:])
                return

            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i+1, cur, total)
        dfs(0, [],0)
        return res


# ✅ Time Complexity:
# O(2^T), where T = target

# In the worst case, every recursive call either includes a candidate (again) or skips to the next candidate.

# This gives a binary recursion tree, with a maximum depth proportional to the target (in the worst case, like [1,1,1,...] summing to target).

# So the number of possible combinations is exponential in target.

# Hence:



# Time complexity ≈ O(2^T)
# More formally, it's closer to O(N^(T/MIN)) where:

# N = number of candidates,

# T = target value,

# MIN = smallest candidate value (because it bounds the recursion depth).

# But for most complexity discussions, we simplify it to exponential in target.

# 📦 Space Complexity:
# O(T) (for recursion stack)
# O(R × L) (for result list)

# Recursive stack can go as deep as target in the worst case ([1,1,1,...] up to target).

# Result list (res) stores all valid combinations:

# Let R be the number of valid combinations.

# Let L be the average length of each combination.
