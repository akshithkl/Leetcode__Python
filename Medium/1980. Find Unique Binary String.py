class Solution(object):
    def findDifferentBinaryString(self, nums):
  
        str_set = {s for s in nums}

        def backtrack(i, cur):
            if i == len(nums):
                res = "".join(cur)
                return None if res in str_set else res
            
            res = backtrack(i + 1, cur)
            if res:
                return res
            
            cur[i] = "1"
            res = backtrack(i + 1, cur)
            if res:
                return res
            
        return backtrack(0, ["0" for s in nums])

# | Aspect               | Value                         |
# | -------------------- | ----------------------------- |
# | **Algorithm**        | Backtracking                  |
# | **Approach**         | Generate binary strings       |
# | **Technique**        | DFS, early stopping           |
# | **Time Complexity**  | `O(n * 2^n)`                  |
# | **Space Complexity** | `O(n + 2^n)`                  |
# | **Best Case**        | Early match, closer to `O(n)` |
# | **Worst Case**       | Explore full space            |
