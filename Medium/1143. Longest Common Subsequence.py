class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        prev = [0] * (n + 1)
        curr = [0] * (n + 1)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    curr[j] = 1 + prev[j + 1]
                else:
                    curr[j] = max(curr[j + 1], prev[j])
            prev, curr = curr, [0] * (n + 1)

        return prev[0]


# | Metric           | Value                                                |
# | ---------------- | ---------------------------------------------------- |
# | Time Complexity  | `O(m * n)`                                           |
# | Space Complexity | `O(n)`                                               |
# | Technique        | Dynamic Programming (Tabulation with Rolling Arrays) |
# | Approach         | Bottom-Up                                            |
