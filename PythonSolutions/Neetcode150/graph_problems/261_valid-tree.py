class DFSSolution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)

        # Create an undirected graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        def dfs(node, prev):
            """
            Prev is used to keep track of what the previous node we was that we just traversed from.
            Prevents incorrect cycle detection in undirected graphs.
            """
            # Base case 1: There is a cycle
            if node in visited:
                return False
            
            # Visit the vertex
            visited.add(node)

            # Explore the neighbors for the current node
            for nei in graph[node]:
                # Base case 2: Skip an incorrect cycle detection from previous node
                if nei == prev:
                    continue
                
                # Explore the current neighbor and make the current node the new previous node
                if not dfs(nei, node):
                    return False

            # No cycle was found, return True
            return True
        
        # Not valid tree check 1: There is a cycle in the graph
            # - Begins search at node 0
            # - Previous node is -1 which doesn't exist yet since there is no current prev node
            # - Only 1 DFS call is needed since we don't care about disconnected components
        if not dfs(0, -1):
            return False
        
        # Not valid tree check 2: There are more than 1 component
            # Checks if we've visited the correct amount of nodes compared to the size of nodes
            # If we have not visited all nodes, then that means that are more than 1 components
        return len(visited) == n

class UnionFind:
    def __init__(self, size):
        self.size = size

        # Create the beginning of root and rank using size
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        # Check if it is a root of itsself, if not flatten the tree so its easier to search
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        # Cycle detection: Check if the nodes we are connecting are in the same component
        if rootX == rootY:
            return False
        
        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        elif self.rank[rootY] > self.rank[rootX]:
            self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1
        
        # Return True since no cycle was detected
        return True
class UnionFindSolution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)

        for u, v in edges:
            # Valid tree check 1: Check if theres any cycles between the union of two nodes
            if not uf.union(u, v):
                return False
        
        # Valid tree check 2: Ensure that there are only 1 root node (1 component)
            # - Since the path has been compressed there should only be 1 root node for 1 component
            # - If [1, 1, 1, 1] as an example, it is all the same root nodes set([1, 1, 1, 1]) == length 1, so only 1 connection
        return len(set([uf.find(i) for i in range(n)])) == 1
        