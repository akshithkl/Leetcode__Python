class Solution(object):
    def wordBreak(self, s, wordDict):

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                
                if dp[i]:
                    break
            
        return dp[0]


# Time Complexity	O(n * k * m)
# Space Complexity	O(n)

# | **Aspect**           | **Value**                                  |
# | -------------------- | ------------------------------------------ |
# | **Algorithm**        | Dynamic Programming                        |
# | **Approach**         | Bottom-Up Tabulation                       |
# | **Technique**        | String Matching + Early Termination        |
# | **Best Case**        | Early match in `wordDict` (fast `break`)   |
# | **Worst Case**       | All combinations checked (no early breaks) |
