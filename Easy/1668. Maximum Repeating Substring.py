class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n, m = len(sequence), len(word)
        memo = {}

        def dp(i):
            # if already computed
            if i in memo:
                return memo[i]

            # base case
            if i < m - 1:
                memo[i] = 0
                return 0

            # check if word matches ending at index i
            if sequence[i - m + 1 : i + 1] == word:
                memo[i] = 1 + dp(i - m)
            else:
                memo[i] = 0
            return memo[i]

        ans = 0
        for i in range(n):
            ans = max(ans, dp(i))
        return ans

# | Aspect                  | Details                                         |
# | ----------------------- | ----------------------------------------------- |
# | **Algorithm Technique** | Dynamic Programming (Top-Down with Memoization) |
# | **Time Complexity**     | O(n · m)                                        |
# | **Space Complexity**    | O(n)                                            |
