class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        res = 0

        while l <= r:
            mid = (l + r) // 2
            coins = (mid / 2) * (mid + 1)
            if coins > n:
                r = mid - 1
            else:
                l = mid + 1
                res = max(res, mid)
        return res


# Time: O(log n)
# Because binary search is used between 1 and n.

# Space: O(1)
# No extra space used apart from a few variables.

# Algorithm Approach
# Technique Used: Binary Search

# Why Binary Search?: The number of coins needed to form k complete rows follows the sum formula:

# coins needed =𝑘(𝑘+1)2coins needed= 2k(k+1)
# ​
 
# This is a monotonically increasing function, so binary search is ideal for finding the maximum k such that: 𝑘(𝑘+1)2≤𝑛 
