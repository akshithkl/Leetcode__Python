class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:       
        nums.sort()
        total = 0

        for i in range(0, len(nums), 2):
            total += nums[i]  
        return total

# | Property             | Value                       |
# | -------------------- | --------------------------- |
# | **Approach**         | Greedy Algorithm            |
# | **Time Complexity**  | `O(n log n)`                |
# | **Space Complexity** | `O(1)` (in-place) or `O(n)` |
# | **Technique**        | Sort + Greedy pairing       |
