class UnionFind:
    def __init__(self):
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
        uf = UnionFind()

        for x, y in edges:
            if not uf.union(x,y):
                return [x,y]
        
        return []