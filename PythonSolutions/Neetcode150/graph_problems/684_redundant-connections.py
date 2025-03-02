class UnionFind:
    def __init__(self):
        # Size is not given so create an empty dict
        self.root = {}
        self.rank = {}
    
    def find(self, x):
        # If the node does not exist yet in the tree, add it
        if x not in self.root:
            self.root[x] = x
            self.rank[x] = 1
        
        # Check if the node is a root of itsself, if not flatten the structure of the tree
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        # If root X and and root Y are the same, then that means the two trees exist in the same component
            # This means a cycle will be created if we union both x and y
        if rootX == rootY:
            return True
        
        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        elif self.rank[rootY] > self.rank[rootX]:
            self.root[rootX] = rootY
        else:
            self.root[rootX] = rootY
            self.rank[rootY] = rootX
        
        # Return false since no cycle will be created at this point
        return False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind()

        for u, v in edges:
            if uf.union(u, v):
                return [u, v]
        
        return []

class DFSSolution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.graph = defaultdict(list)

        for u, v in edges:
            # Create a new set every DFS call to check if there is a path between source and target
            visited = set()

            # Check:
                # - If u and v are in the graph before calling a DFS between the two nodes
                # - Prevents DFS since if these nodes don't exist then we can't find a path from source to target
                # *- Run DFS to check if there's an existing path between source and target, if there is then a cycle will be created*
            if u in self.graph and v in self.graph and self.dfs(u, v, visited):
                # Return the edge that creates a cycle
                return [u, v]
            
            # Connect the edges to the graph unidirectionally
            self.graph[u].append(v)
            self.graph[v].append(u)
        
        return []
    
    def dfs(self, source, target, visited):
        # Base case 1: Check if we end up finding an existing path to target already
        if source == target:
            return True
        
        # Base case 2: Check if we have already visited the node
        if source in visited:
            return False
        
        visited.add(source)

        # Explore all neighbors until we possibly find the target node
        for nei in self.graph[source]:
            if self.dfs(nei, target, visited):
                return True
        
        # Return False since we could not find a valid path to target
        return False