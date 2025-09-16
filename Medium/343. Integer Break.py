class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}

        def dfs(num):
            if num in memo:
                return memo[num]
            if num == 1:
                return 1

            best = 0
            for j in range(1, num):
                best = max(best, j * (num - j), j * dfs(num - j))

            memo[num] = best
            return best

        return dfs(n)

# Approach/Technique: DP – Top Down with Memoization
# Time Complexity: O(n²)
# Space Complexity: O(n)
