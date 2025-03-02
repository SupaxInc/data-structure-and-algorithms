class DFSSolution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        # Create an undirected graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        
        def dfs(node):
            # Base case 1: If its already been visited then return 0
                # - Means that we've already counted it as a component from a previous DFS
            if node in visited:
                return 0
            
            # Visit the vertex
            visited.add(node)

            # Explore the neighbors
            for nei in graph[node]:
                dfs(nei)

            # No need to unvisit the vertex
                # - Compared to topological sort, it requires backtracking since we need to know if the next courses can complete the prerequisites
                # - However, here we just need to visit all nodes to ensure its 1 connected component
            
            # Return a 1 after exploring all neighbors for current DFS, this counts as 1 component
            return 1
        
        count = 0
        # Run a DFS across all nodes in the case of disconnected components
        for node in range(n):
            # Only run DFS on nodes we have not visited, premature optimization
            if node not in visited:
                count += dfs(node)
        
        return count

class UnionFind:
    def __init__(self, size: int):
        self.size = size
        # During initialization, all nodes are roots of itsself
            # E.g. [0, 1, 2, 3, 4], index 0 (root 0) is parent of itsself, etc
        self.root = [i for i in range(size)]
        # During initialization, all nodes have a rank of 1
            # E.g. [1, 1, 1, 1, 1]
        self.rank = [1] * size
    
    def find(self, x):
        """Find the root node for target node"""
        # Check if the target node is connected to a root node
            # By checking if the value of the node points to the index of itsself
        if self.root[x] != x:
            # If its not a root of itsself, then recursively flatten the tree until it is
            # E.g. [0, 0, 1] , index 2 (root 2) points to index 1, index 1 points to index 0
            self.root[x] = self.find(self.root[x])
        # E.g. [0, 0, 1] becomes [0, 0, 0]
        return self.root[x]
    
    def union(self, x, y):
        """Connect node x and node y together based on ranks"""
        # Find the root nodes for each target nodes so we can connect them by root
        rootX = self.find(x)
        rootY = self.find(y)

        # Connect the smaller tree to the larger tree (size is based on rank)
        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        elif self.rank[rootY] > self.rank[rootX]:
            self.root[rootX] = rootY
        else:
            # If both trees are of same rank then just choose any root to connect to
            self.root[rootX] = rootY
            # Depending on root you connect to increase the rank by 1
                # Because the longest path in each tree is now part of the longest path in the new tree, resulting in a taller tree.
            self.rank[rootY] += 1

class UnionFindSolution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create the disjoint set of size n
        uf = UnionFind(n)

        # Connect the root nodes using the edge list
        for u, v in edges:
            uf.union(u, v)
        
        # Count the components by finding the amount of the root nodes
            # Run the find for each node, essentially adding it to an array
            # Create a set since we a graph could be all pointing to 1 root node
        return len(set([uf.find(i) for i in range(n)]))
