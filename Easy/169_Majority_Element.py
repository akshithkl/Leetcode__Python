class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        res = 0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)

        return res


# Algorithm / Technique: Boyer-Moore Majority Vote Algorithm

# Approach: Greedy / Voting Approach
        
# ✅ Time and Space Complexity
# ⏱ Time Complexity: O(n)
# You make a single pass through the array nums.

# Each operation inside the loop is O(1), so the total time is proportional to the size of nums.

# 🧠 Space Complexity: O(1)
# Only a few variables (count, res) are used.

# No extra space is used that scales with input size.


        
