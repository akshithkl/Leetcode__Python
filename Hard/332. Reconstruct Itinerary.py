class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        
        # Use a min-heap for each src to maintain lexicographical order
        for src, dst in tickets:
            heapq.heappush(adj[src], dst)

        res = []

        def dfs(src):
            while adj[src]:
                next_dest = heapq.heappop(adj[src])
                dfs(next_dest)
            res.append(src)

        dfs("JFK")
        return res[::-1]



# | Part               | Complexity                                            |
# | ------------------ | ----------------------------------------------------- |
# | **Time**           | `O(n log n)`                                          |
# | **Space**          | `O(n)`                                                |
# | **Technique Used** | DFS + Min-Heap                                        |
# | **Algorithm**      | Hierholzer’s Algorithm (Eulerian Path) with Lex Order |
