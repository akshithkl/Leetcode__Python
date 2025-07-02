class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
 
        # Step 1: Build the graph
        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)

        for u, v in redEdges:
            red_graph[u].append(v)
        for u, v in blueEdges:
            blue_graph[u].append(v)

        # Step 2: Initialize answer and visited tracking
        answer = [-1] * n
        visited = [[False, False] for _ in range(n)]  # visited[node][color]

        # Step 3: BFS queue -> (node, steps, last_color)
        queue = deque()
        queue.append((0, 0, -1))  # Start with node 0, 0 steps, no previous color

        while queue:
            node, steps, last_color = queue.popleft()

            if answer[node] == -1:
                answer[node] = steps

            # If last color was not red, explore red edges
            if last_color != 0:
                for nei in red_graph[node]:
                    if not visited[nei][0]:
                        visited[nei][0] = True
                        queue.append((nei, steps + 1, 0))

            # If last color was not blue, explore blue edges
            if last_color != 1:
                for nei in blue_graph[node]:
                    if not visited[nei][1]:
                        visited[nei][1] = True
                        queue.append((nei, steps + 1, 1))

        return answer  


#         | Aspect               | Value                           |
# | -------------------- | ------------------------------- |
# | **Algorithm**        | BFS with color tracking         |
# | **Technique**        | Level-wise BFS + visited matrix |
# | **Time Complexity**  | `O(n + r + b)`                  |
# | **Space Complexity** | `O(n + r + b)`                  |
# | **Best for**         | Shortest path with constraints  |
