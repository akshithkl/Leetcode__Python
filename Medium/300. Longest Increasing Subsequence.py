class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)

# | Aspect           | Value                 |
# | ---------------- | --------------------- |
# | Algorithm        | Dynamic Programming   |
# | Approach         | Bottom-Up Tabulation  |
# | Technique        | DP, Reverse Iteration |
# | Time Complexity  | O(n²)                 |
# | Space Complexity | O(n)                  |
