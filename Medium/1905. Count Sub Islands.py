class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        Rows = len(grid1)
        Cols = len(grid1[0])
        visit = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or r == Rows or c == Cols or grid2[r][c] == 0 or (r, c) in visit):
                return True

            visit.add((r, c))
            res = True
            if grid1[r][c] == 0:
                res =  False
            
            res = dfs(r - 1, c) and res
            res = dfs(r + 1, c) and res
            res = dfs(r, c - 1) and res
            res = dfs(r, c + 1) and res

            return res
        
        count = 0
        for r in range(Rows):
            for c in range(Cols):
                if grid2[r][c] and (r, c) not in visit and dfs(r, c):
                    count += 1
        
        return count


# | **Aspect**             | **Details**                                                                                   |
# | ---------------------- | --------------------------------------------------------------------------------------------- |
# | **Algorithm**          | DFS (Depth-First Search)                                                                      |
# | **Approach/Technique** | Graph traversal + validation                                                                  |
# | **Time Complexity**    | **O(R × C)** (visit each cell once at most)                                                   |
# | **Space Complexity**   | **O(R × C)** for `visit` set + recursion stack                                                |
# | **Key Idea**           | An island in `grid2` is a sub-island only if all its land cells overlap with land in `grid1`. |
