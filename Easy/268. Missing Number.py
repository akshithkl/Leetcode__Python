class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])

        return res

# | Aspect               | Value                                  |
# | -------------------- | -------------------------------------- |
# | **Time Complexity**  | O(n) (single loop over nums)           |
# | **Space Complexity** | O(1) (no extra space used)             |
# | **Technique Used**   | Arithmetic sum difference / math trick |
