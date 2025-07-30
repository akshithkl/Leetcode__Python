class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        for p in [2, 3, 5]:
            while n % p == 0:
                n = n// p
        
        return n == 1

# Time Complexity: O(log n) – At worst, you're dividing n by 2, 3, and 5 repeatedly.
# Space Complexity: O(1) – No extra space use
