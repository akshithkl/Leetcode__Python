class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = [0] * (len(triangle) + 1)
        for row in triangle[:: -1]:
            for i, n in enumerate(row):
                dp[i] = n + min(dp[i], dp[i+1])
            
        return dp[0]



# | Time Complexity  | O(n²) |
# | Space Complexity | O(n)  |
