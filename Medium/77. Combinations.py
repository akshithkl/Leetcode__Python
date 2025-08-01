class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb[:])
                return
            
            for i in range(start, n + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()

        backtrack(1, [])
        return res

# | Item                 | Value                            |
# | -------------------- | -------------------------------- |
# | **Algorithm**        | Backtracking (DFS)               |
# | **Time Complexity**  | $O(\binom{n}{k} \cdot k)$        |
# | **Space Complexity** | $O(k) + O(\binom{n}{k} \cdot k)$ |
# | **Use Case**         | Generating combinations          |
