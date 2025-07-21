class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to prereq list
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True

            visitSet.add(crs) 
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True
            
        for crs in range(numCourses):
            if not dfs(crs): return False
            
        return True


# Algorithm: Depth-First Search (DFS)
# Approach: Topological Sort using DFS + cycle detection
# Technique: Graph traversal, Backtracking


# Time Complexity: O(V + E)
# V = number of courses (vertices)
# E = number of prerequisites (edges)
# Space Complexity: O(V + E)
