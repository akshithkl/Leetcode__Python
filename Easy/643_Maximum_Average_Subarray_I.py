class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window = sum(nums[:k])
        max_avg = window* 1.0 / k

        for i in range(k, len(nums)):
            window += nums[i] - nums[i - k]
            max_avg = max(max_avg, window * 1.0 / k)
        
        return max_avg



#  Time Complexity: O(n)
# sum(nums[:k]) takes O(k) time.

# The loop from k to len(nums) takes O(n - k) time.

# So, total time = O(k + (n - k)) = O(n)

# Space Complexity: O(1)
# You're using only a few variables (window, max_avg), regardless of the size of the input.

# No extra space proportional to input size.
