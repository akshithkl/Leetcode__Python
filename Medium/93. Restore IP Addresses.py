class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res  =[] 
        if len(s) > 12:
            return res
        
        def backtrack(i, dots, curIP):
            if dots == 4 and i == len(s):
                res.append(curIP[:-1])
                return
            
            if dots > 4:
                return 
            for j in range(i, min(i + 3, len(s))):
                if int(s[i:j+1]) < 256 and (i == j or s[i] != "0"):
                    backtrack(j+1, dots + 1, curIP + s[i:j+1] + ".") 

        backtrack(0, 0, "")
        return res       

# | Property             | Value                                 |
# | -------------------- | ------------------------------------- |
# | **Algorithm**        | Backtracking                          |
# | **Approach**         | DFS with dot placement                |
# | **Technique**        | Recursion + pruning                   |
# | **Time Complexity**  | O(1) → fixed upper limit (≤ 81 cases) |
# | **Space Complexity** | O(k) → where k is number of valid IPs |
