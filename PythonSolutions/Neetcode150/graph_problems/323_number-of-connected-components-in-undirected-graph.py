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

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if self.root[x] != x:
            # If node does not equal itself, recursively find the parent then compress the path
            # It will point the child directly to parent node instead of creating a linked list
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Connect the root to the greatest rank between the two roots
                # This also prevents a linked list from happening to the parent node
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
    


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        unionFind = UnionFind(n)

        # Connect together the different roots based on edges
        for x, y in edges:
            unionFind.union(x, y)
        
        # Applying find to each node to ensure path compression
            # Creates a set of parent nodes so we can find the length of all parent nodes
            # This tells us the different groups of connections
        return len(set(unionFind.find(i) for i in range(n)))
