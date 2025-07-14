class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        digitToChar = { "2" : "abc",
                        "3" : "def",
                        "4" : "ghi",
                        "5" : "jkl",
                        "6" : "mno",
                        "7" : "pqrs",
                        "8" : "tuv",
                        "9" : "wxyz" }
        
        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)
        
        if digits:
            backtrack(0, "")
        
        return res


# | Aspect               | Value                                   |
# | -------------------- | --------------------------------------- |
# | **Algorithm**        | Backtracking                            |
# | **Approach**         | DFS with recursion                      |
# | **Technique**        | Recursive Tree Traversal                |
# | **Time Complexity**  | $O(4^n)$                                |
# | **Space Complexity** | $O(n \cdot 4^n)$                        |
# | **Best Case**        | Still $O(3^n)$ if all digits are 2–6, 8 |
