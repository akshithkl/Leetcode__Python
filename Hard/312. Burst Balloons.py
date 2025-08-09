class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0
            
            if (l, r) in dp:
                return dp[(l, r)]
            
            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)
            
            return dp[(l, r)]
        
        return dfs(1, len(nums) - 2)
       

# | **Aspect**           | **Details**                                                                                               |
# | -------------------- | --------------------------------------------------------------------------------------------------------- |
# | **Problem**          | LeetCode 312 — Burst Balloons                                                                             |
# | **Approach**         | **Interval Dynamic Programming** (Top-Down Memoization)                                                   |
# | **State Definition** | `dp[(l, r)]` → Max coins obtainable by bursting balloons between indexes `l` and `r` (inclusive)          |
# | **Transition**       | `dp[(l, r)] = max(nums[l-1] * nums[i] * nums[r+1] + dp[(l, i-1)] + dp[(i+1, r)])` for all `i` in `[l, r]` |
# | **Base Case**        | If `l > r` → return `0` (no balloons to burst)                                                            |
# | **Number of States** | `O(n²)` (all `(l, r)` pairs)                                                                              |
# | **Work per State**   | `O(n)` (looping over possible `i` to burst last)                                                          |
# | **Time Complexity**  | **O(n³)**                                                                                                 |
# | **Space Complexity** | **O(n²)** for memoization + **O(n)** recursion stack → Overall **O(n²)**                                  |
# | **Algorithm Type**   | Dynamic Programming → Top-Down with Memoization                                                           |
# | **Why Efficient**    | Each subproblem `(l, r)` is computed once, and overlapping subproblems are cached                         |


        
