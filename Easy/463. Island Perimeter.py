class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()
        
        def dfs(r, c):
            if r >= len(grid) or c >= len(grid[0]) or \
               r < 0 or c < 0 or grid[r][c] == 0:
               return 1
            if (r, c) in visit:
                return 0
            
            visit.add((r, c))         
            perimeter = dfs(r, c + 1)
            perimeter += dfs(r + 1, c)
            perimeter += dfs(r - 1, c)
            perimeter += dfs(r, c - 1)  
            return perimeter

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    return dfs(r,c)

# | Aspect               | Details                                                                                           |
# | -------------------- | ------------------------------------------------------------------------------------------------- |
# | **Algorithm**        | DFS (Depth-First Search)                                                                          |
# | **Time Complexity**  | `O(m * n)`                                                                                        |
# | **Space Complexity** | `O(m * n)` (visited set + recursion stack)                                                        |
# | **Why Efficient**    | Each land cell is processed only once, perimeter is counted directly from DFS boundary conditions |
