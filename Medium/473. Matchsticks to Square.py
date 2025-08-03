class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        length = sum(matchsticks) // 4
        sides = [0] * 4

        if sum(matchsticks) / 4 != length:
            return False
        matchsticks.sort(reverse=True) 
        def backtrack(i):
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                if sides[j] + matchsticks[i] <= length:
                    sides[j] += matchsticks[i]
                    if backtrack(i + 1):
                        return True
                    sides[j] -= matchsticks[i]
                if sides[j] == 0:
                    break
            return False
        return backtrack(0)

# | Aspect                           | Value                                |
# | -------------------------------- | ------------------------------------ |
# | **Approach**                     | Backtracking with pruning            |
# | **Heuristic**                    | Sort matchsticks in descending order |
# | **Time Complexity (worst case)** | `O(4^N)`                             |
# | **Space Complexity**             | `O(N)` (recursion stack)             |
# | **Type of problem**              | Partition / Subset Sum Variation     |
