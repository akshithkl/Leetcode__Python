class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_len = 1
        curr_len = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr_len += 1
                max_len = max(max_len, curr_len)
            else:
                curr_len = 1  # reset for new subarray

        return max_len
        
# | Feature       | Description                                                   |
# | ------------- | ------------------------------------------------------------- |
# | **Approach**  | Greedy + Sliding Window                                       |
# | **Time**      | O(n)                                                          |
# | **Space**     | O(1)                                                          |


        
