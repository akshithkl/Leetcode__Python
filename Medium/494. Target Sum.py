class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = {}

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = (backtrack(i+1, total + nums[i]) +
                              backtrack(i+1, total - nums[i]))
            return dp[(i, total)]
        
        return backtrack(0, 0)


# | Aspect               | Description                               |
# | -------------------- | ----------------------------------------- |
# | **Algorithm**        | Top-down Dynamic Programming (with memo)  |
# | **Approach**         | Backtracking + Memoization (Recursive DP) |
# | **Technique**        | DFS-style recursion + DP cache            |
# | **Time Complexity**  | `O(n * sum(nums))`                        |
# | **Space Complexity** | `O(n * sum(nums))`                        |
