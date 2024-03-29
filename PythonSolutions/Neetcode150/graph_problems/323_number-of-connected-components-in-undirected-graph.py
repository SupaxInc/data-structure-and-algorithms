class DFSSolution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = { v: [] for v in range(0, n) }
        visited = set()
        count = 0

        # Create a bi-directional graph
        for v, e in edges:
            graph[v].append(e)
            graph[e].append(v)

        def dfs(v):
            # If a vertex is already visited return a 0
            if v in visited:
                return 0
            
            # Visit all edges in 1 DFS for 1 connected component
                # All vertices should be connected to each other since its undirected
            visited.add(v)
            for e in graph[v]:
                dfs(e)
            
            # If a vertex has not been visited return a 1
            return 1

        
        for v in range(0, n):
            count += dfs(v)
        
        return count