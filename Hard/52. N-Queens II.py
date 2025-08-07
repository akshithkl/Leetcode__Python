class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posDiag = set()
        negDiag = set()

        res = 0 
        def backtrack(r):
            if r == n:
                nonlocal res
                res += 1
                return n
                
            
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
            return res
        
        return backtrack(0)

# | Aspect               | Value                                      |
# | -------------------- | ------------------------------------------ |
# | **Technique**        | Backtracking with Pruning                  |
# | **Time Complexity**  | O(N!)                                      |
# | **Space Complexity** | O(N)                                       |
# | **Optimization**     | Uses sets to avoid invalid positions early |


            
