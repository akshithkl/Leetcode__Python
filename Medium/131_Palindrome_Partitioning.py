class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(list(part))
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return res
    
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True


# | Metric                     | Complexity   |
# | -------------------------- | ------------ |
# | **Time**                   | `O(2^n * n)` |
# | **Space (total)**          | `O(n * 2^n)` |
# | **Space (recursion only)** | `O(n)`       |
