class DFSSolution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        visited = set()
        graph = {v: [] for v in range(n)}

        # Create an bi-directional graph (undirected)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(source, prev):
            # Check if a cycle is detected
            if source in visited:
                return False
            
            visited.add(source)
            for adj in graph[source]:
                # Don't do a DFS on the neighbor we just traversed from since we have visited it already
                    # Prevents detecting a cycle this way
                if adj == prev:
                    continue
                
                # Explore the next neighbors and add the current node we are on as the previous
                if not dfs(adj, source):
                    return False
            
            return True
        
        # DFS checks if there is a cycle
        # Length of visited checks if all of the vertices are connected
        return dfs(0, -1) and len(visited) == n

class UnionFind:
    def __init__(self, size):
        self.parent = [n for n in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)

        if parentX == parentY:
            return False
        else:
            if self.rank[parentX] > self.rank[parentY]:
                self.parent[parentY] = parentX
            elif self.rank[parentX] < self.rank[parentY]:
                self.parent[parentX] = parentY
            else:
                self.parent[parentY] = parentX
                self.rank[parentX] += 1
        
        return True

class UnionFindSolution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)

        for x, y in edges:
            # Check for loops in the graph
            if not uf.union(x, y):
                return False

        # Check if there is only one connection, since if theres more than 1 thats not a valid tree
        return len(set(uf.find(x) for x in range(n))) == 1