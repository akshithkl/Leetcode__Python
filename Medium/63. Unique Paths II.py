class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [0] * n
        dp[n-1] = 1

        for r in reversed(range(m)):
            for c in reversed(range(n)):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                elif c + 1 < n:
                    dp[c] = dp[c] + dp[c + 1]
        
        return dp[0]
        
# | Aspect               | Details                                                      |
# | -------------------- | ------------------------------------------------------------ |
# | **Algorithm**        | Dynamic Programming (Bottom-Up, Tabulation, Space Optimized) |
# | **Time Complexity**  | `O(m * n)`                                                   |
# | **Space Complexity** | `O(n)` (1D DP array)                                         |
# | **Why Optimized**    | Instead of `dp[m][n]`, only 1D array `dp[n]` is maintained   |

        
