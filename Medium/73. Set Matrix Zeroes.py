class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows, cols = len(matrix), len(matrix[0])
        first_row_zero = False
        first_col_zero = False

        # Step 1: check if first row and first column need to be zero
        for c in range(cols):
            if matrix[0][c] == 0:
                first_row_zero = True
        for r in range(rows):
            if matrix[r][0] == 0:
                first_col_zero = True

        # Step 2: use first row & col as markers
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # Step 3: set cells to zero based on markers
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Step 4: handle first row and first column
        if first_row_zero:
            for c in range(cols):
                matrix[0][c] = 0
        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0
        
# | **Aspect**             | **Details**                                                |
# | ---------------------- | ---------------------------------------------------------- |
# | **Algorithm**          | In-place Matrix Marking (using first row & col as markers) |
# | **Approach/Technique** | Matrix traversal + marker-based update                     |
# | **Time Complexity**    | **O(m × n)** (visit each cell at most twice)               |
# | **Space Complexity**   | **O(1)** (constant space, aside from input matrix)         |
# | **Key Idea**           | Use first row & col as markers to avoid extra memory       |
