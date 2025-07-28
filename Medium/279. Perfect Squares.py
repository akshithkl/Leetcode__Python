class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0

        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s

                if target - square < 0:
                    break
                
                dp[target] = min(dp[target], 1 + dp[target - square])
        
        return dp[n]

        

# | **Aspect**             | **Details**                                                        |
# | ---------------------- | ------------------------------------------------------------------ |
# | **Problem**            | Perfect Squares (LeetCode 279)                                     |
# | **Approach**           | Bottom-Up Dynamic Programming (Tabulation)                         |
# | **DP State**           | `dp[i]` = minimum number of perfect squares that sum to `i`        |
# | **Initialization**     | `dp[0] = 0`; all others initialized to `n` (worst case)            |
# | **Transition Formula** | `dp[target] = min(dp[target], 1 + dp[target - square])`            |
# | **Loop Structure**     | Outer: `target` from `1` to `n` <br> Inner: all squares ≤ `target` |
# | **Time Complexity**    | O(n \cdot \sqrt{n})$                                              |
# | **Space Complexity**   | O(n)
