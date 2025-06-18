class Solution(object):
    def maxRotateFunction(self, nums):
        n = len(nums)
        total_sum = sum(nums)
        f = sum(i * num for i, num in enumerate(nums))
        max_value = f

        for i in range(1, n):
            f += total_sum - n * nums[-i]
            max_value = max(max_value, f)

        return max_value

#  Dynamic Bottom up

# ⏱️ Time Complexity
# sum(nums) → O(n)

# sum(i * num for i, num in enumerate(nums)) → O(n)

# Loop from 1 to n-1 → O(n)

# So,
# Time Complexiy=𝑂(𝑛)
# Time Complexity= 
# O(n)
# ​
 
# 📦 Space Complexity
# We use only a constant number of variables: n, total_sum, f, max_value

# No additional data structures are created.So,

# Space Complexity=𝑂(1)
# Space Complexity= O(1)
# ​
 
