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
        self.root = [n for n in range(size)]
        self.rank = [1] * size
    
    def find(self, x):
        # Check if the index equals its value (it is its own root node, does not point to another root)
        if self.root[x] != x:
            # Go as deep as possible to find the root node
                # (the node where its index equals its value)
                # E.g. [0, 0, 1] , index 2 (root 2) points to index 1, index 1 points to index 0
                    # 0 is the parent node of all nodes
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)

        # Cycle is detected if an edges pair have the same vertices in the same component
        if parentX == parentY:
            return False
        else:
            # Connect the root with the smallest rank (smaller tree) to the root has a larger rank
                # If its the same rank then just choose whatever
            if self.rank[parentX] > self.rank[parentY]:
                # No need to add a rank as the structure is flattened
                self.root[parentY] = parentX
            elif self.rank[parentX] < self.rank[parentY]:
                # No need to add a rank as the structure is flattened
                self.root[parentX] = parentY
            else:
                self.root[parentX] = parentY
                # Add a rank since
                # Longest path in each tree is now part of the longest path in the new tree, resulting in a taller tree.
                self.rank[parentY] += 1
        
        return True


class UnionFindSolution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)

        for x, y in edges:
            # Checking for cycles, if an edges pair has the same vertex then it connects to same component
            if not uf.union(x, y):
                return False

        # Check if there is only one connection, since if theres more than 1 thats not a valid tree
            # It will compress the paths for each node to 1 singular parent node
            # If it returns more than one different node and is created as a set with a greater length of 1, that means there are multiple connections
            # If [1, 1, 1, 1] as an example, it is all the same root nodes set([1, 1, 1, 1]) == length 1, so only 1 connection
        return len(set([uf.find(x) for x in range(n)])) == 1
        