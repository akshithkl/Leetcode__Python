class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0 : 1}

        for total in range(1, target + 1):
            dp[total] = 0
            for n in nums:
                dp[total] += dp.get(total - n, 0)
        return dp[target]

# | **Metric**           | **Value**                       |
# | -------------------- | ------------------------------- |
# | **Algorithm**        | Dynamic Programming             |
# | **Approach**         | Bottom-Up (Tabulation)          |
# | **Technique**        | Unbounded Knapsack (with order) |
# | **Time Complexity**  | `O(target × len(nums))`         |
# | **Space Complexity** | `O(target)`                     |
# | **Best For**         | Ordered combinations with reuse |
