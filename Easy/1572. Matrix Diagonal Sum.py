class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = 0

        for i in range(n):
            # Primary diagonal
            total += mat[i][i]
            # Secondary diagonal
            total += mat[i][n - i - 1]

        # Subtract the middle element (if n is odd, it's counted twice)
        if n % 2 == 1:
            total -= mat[n // 2][n // 2]

        return total

# | Metric                 | Value                                                                                            |
# | ---------------------- | ------------------------------------------------------------------------------------------------ |
# | **Algorithm Approach** | **Iterative Summation** (direct index-based access)                                              |
# | **Technique**          | **Single-pass iteration** over rows                                                              |
# | **Time Complexity**    | **O(n)** → We only loop once through `n` rows, adding two values (primary & secondary diagonal). |
# | **Space Complexity**   | **O(1)** → No extra data structures are used, just a few variables for sum.                      |
