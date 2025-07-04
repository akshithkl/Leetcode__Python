class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        
        return dp[amount] if dp[amount] != amount + 1 else -1


# Time Complexity: O(amount * len(coins))

# Space Complexity: O(amount)

# | Item             | Value                    |
# | ---------------- | ------------------------ |
# | **Technique**    | Dynamic Programming      |
# | **Approach**     | Bottom-up Tabulation     |
# | **Category**     | Unbounded Knapsack       |
# | **Optimization** | Minimize number of coins |
# | **Time**         | O(amount × len(coins))   |
# | **Space**        | O(amount)                |
