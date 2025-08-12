class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n = len(strs), len(strs[0])
        delete_count = 0

        for col in range(n):
            for row in range(m - 1):
                if strs[row][col] > strs[row + 1][col]:
                    delete_count += 1
                    break  # No need to check further for this column
        return delete_count

# | Aspect              | Details                                              |
# | ------------------- | ---------------------------------------------------- |
# | Algorithm technique | Brute-force column-wise check (simulation)           |
# | Time Complexity     | O(m × n), m = rows, n = columns                       |
# | Space Complexity    | O(1), no extra data structures used                   |
# | Paradigm            | Direct comparison / linear scan in each column       |
# | Data Structure      | 2D character grid (implicit from list of strings)    |
