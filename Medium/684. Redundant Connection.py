class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        rank = [0] * (n + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # path compression
            return parent[x]

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False  # already connected -> cycle
            # union by rank
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]

        return []  # should not reach here



# | Approach / Technique    | Algorithm Used                                                           | Time Complexity        | Space Complexity                          | Notes                                                              |
# | ----------------------- | ------------------------------------------------------------------------ | ---------------------- | ----------------------------------------- | ------------------------------------------------------------------ |
# | **Union–Find (DSU)**    | Disjoint Set Union with **Path Compression** + **Union by Rank**         | `O(n α(n))` (≈ `O(n)`) | `O(n)`                                    | Efficient, standard solution. Detects cycle while inserting edges. |
# | **DFS Cycle Detection** | Depth-First Search for each edge to check if nodes are already connected | `O(n^2)` (worst case)  | `O(n)` (recursion stack + adjacency list) | Works but slower; checks connectivity repeatedly.                  |
