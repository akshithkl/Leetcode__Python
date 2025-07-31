class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        def dfs(i, j):
            if j == len(t):  # All of t is matched
                return 1
            if i == len(s):  # Ran out of s before matching all of t
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            
            if s[i] == t[j]:
                # Option 1: match s[i] with t[j], move both i and j
                # Option 2: skip s[i], move only i
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                # Skip s[i], keep j same
                cache[(i, j)] = dfs(i + 1, j)
            
            return cache[(i, j)]
        
        return dfs(0, 0)

# | Aspect               | Value                          |
# | -------------------- | ------------------------------ |
# | **Algorithm Type**   | Dynamic Programming (Top-Down) |
# | **Approach**         | DFS + Memoization              |
# | **Time Complexity**  | O(m × n)                       |
# | **Space Complexity** | O(m × n)                       |
# | **Use Case**         | Count subsequences             |
