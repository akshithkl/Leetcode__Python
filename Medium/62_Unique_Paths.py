class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        row  = [1] * n

        for i in range(m-1):
            newRow = [1] * n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]

# | Feature              | Value                                     |
# | -------------------- | ----------------------------------------- |
# | **Algorithm**        | Dynamic Programming                       |
# | **Technique**        | Bottom-Up Tabulation + Space Optimization |
# | **Time Complexity**  | O(m × n)                                  |
# | **Space Complexity** | O(n)                                      |
