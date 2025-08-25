class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visit, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
            
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output


# | Step / Component            | Complexity   | Reason                                                 |
# | --------------------------- | ------------ | ------------------------------------------------------ |
# | Build adjacency list        | `O(V + E)`   | Initialize `V` courses + insert `E` prerequisite edges |
# | DFS traversal               | `O(V + E)`   | Visit each node once + explore each edge once          |
# | Reversing result (optional) | `O(V)`       | Reverse topological order at the end                   |
# | **Total Time**              | **O(V + E)** | Dominated by graph build + DFS                         |
# | Adjacency list storage      | `O(V + E)`   | Store all edges                                        |
# | `visit` + `cycle` sets      | `O(V)`       | Store at most all nodes                                |
# | Recursion stack             | `O(V)`       | Worst-case depth = all courses chained                 |
# | Output list                 | `O(V)`       | Store topological ordering                             |
# | **Total Space**             | **O(V + E)** | Graph + auxiliary structures                           |
