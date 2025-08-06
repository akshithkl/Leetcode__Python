class Solution:
    def numTrees(self, n: int) -> int:
        numTree = [1] * (n + 1)
        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left = root - 1
                right = nodes - root 
                total += numTree[left] * numTree[right]
            numTree[nodes] = total
        
        return numTree[n]

# | Aspect               | Value                      |
# | -------------------- | -------------------------- |
# | **Approach**         | Dynamic Programming (DP)   |
# | **Technique**        | Bottom-up Tabulation       |
# | **Algorithm**        | Catalan Number Computation |
# | **Time Complexity**  | `O(n^2)`                   |
# | **Space Complexity** | `O(n)`                     |
