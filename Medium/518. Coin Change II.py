class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i: int, target: int) -> int:
            if target == 0:
                return 1
            if i == len(coins) or target < 0:
                return 0
            if (i, target) in memo:
                return memo[(i, target)]

            # Option 1: skip current coin
            skip = dfs(i + 1, target)
            # Option 2: take current coin
            take = dfs(i, target - coins[i])

            memo[(i, target)] = skip + take
            return memo[(i, target)]

        return dfs(0, amount)

# Algorithm → Top-Down DP with Memoization (DFS + caching).
# Time Complexity → O(n × amount)
# Space Complexity → O(n × amount)
