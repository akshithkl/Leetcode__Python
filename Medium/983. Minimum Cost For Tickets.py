class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        
        dp = {}
        n = len(days)

        for i in range(n - 1, -1, -1):  # iterate from end to start
            dp[i] = float("inf")
            for d, c in zip([1, 7, 30], costs):
                j = i
                while j < n and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], c + dp.get(j, 0))

        return dp[0]


# | Attribute            | Value / Explanation                           |
# | -------------------- | --------------------------------------------- |
# | **Algorithm**        | Dynamic Programming                           |
# | **Approach**         | Bottom-Up (Reverse iteration)                 |
# | **Technique**        | Tabulation using dictionary                   |
# | **Time Complexity**  | O(N)                                          |
# | **Space Complexity** | O(N)                                          |
# | **Optimized**        | Yes (no recursion stack used, pure iterative) |
#                  |
