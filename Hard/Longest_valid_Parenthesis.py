class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = 0
        right = 0
        max_lenght = 0

        for x in s:
            if x in '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                max_lenght = max(max_lenght, left+ right)
            elif right > left:
                left = right = 0

        left = right = 0

        for x in s[:: -1]:
            if x in '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                max_lenght = max(max_lenght, left + right)
            elif left > right:
                left = right = 0
        
        return max_lenght
