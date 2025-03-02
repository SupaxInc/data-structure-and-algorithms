class UnionFind:
    def __init__(self):
        # Since theres no size, we use a hashmap
        self.parent = {}
        self.rank = {}
    
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 1
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        # This will continuously create a union between two nodes
        # At some point we end up with a node already in a group
        # Where cycle gets detected below
        parentX = self.find(x)
        parentY = self.find(y)

        # Cycle has been detected
            # When parent nodes equal each other it means the edge that we will connect will form a cycle
            # Due to nodes pointing to parent nodes to show which group the connection it is in
            # If they are in the same group, it means the edge we are connecting will form its own connection
            # Thus creating a loop
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

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind() # No size of graph given

        for x, y in edges:
            if not uf.union(x,y):
                return [x,y]
        
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