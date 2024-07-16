class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        totalVertices = len(points)
        visited = set()

        # Beginning at point 0, so our cost is 0
        # This can be a random known point on the grid/graph but
            # starting at 0,0 is a common strategy for Prims algorithm
        minHeap = [(0, 0)] # (current cost, current point on grid)

        # Manhttan distance is used to calculate the cost of two points
            # Helps determine the smallest edge to add the to MST in Prims algorithm
        def manhattan(i, j):
            # Manhattan distance: (x1 - x2) + (y1 - y2)
            return abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
        
        # Stop Prims algorithm when we have visited total amount of vertices
            # This will create an MST, since totalVertices - 1 = total edges
        while len(visited) < totalVertices:
            currCost, currPoint = heapq.heappop(minHeap)

            # Undirected graph so there is chance we have already visited a point
                # This is needed since we are popping from a min heap
                # That means it will select the minimum cost edge
                # We may end up popping an edge we have already visited since its randomized based on min cost
            if currPoint in visited:
                continue
            
            # Visit the vertex
            visited.add(currPoint)
            res += currCost

            # Traverse all of the other points since the point can be a neighbour to all points
            for nextPoint in range(totalVertices):
                if nextPoint not in visited:
                    heapq.heappush(minHeap, (manhattan(currPoint, nextPoint), nextPoint))
        
        return res
    

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
    
    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # Path compression
        return self.parent[p]
    
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            # Union by rank
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1
            return True
        return False

class UnionFindSolution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        totalVertices = len(points)
        edges = []

        # Generate all possible edges with their weights (Manhattan distances)
        for i in range(totalVertices):
            for j in range(i + 1, totalVertices):
                weight = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((weight, i, j))

        # Sort edges by weight
            # Allows us to select and connect the most minimum weights first for each point
        edges.sort()

        # Kruskal's algorithm to form MST
        uf = UnionFind(totalVertices)
        mst_cost = 0  # Total cost of the MST
        edges_used = 0  # Number of edges added to the MST

        for weight, u, v in edges:
            # Add edges 1 by 1, connecting points (u, v) together to form a graph
                # Check if it doesn't for a cycle
            if uf.union(u, v):  
                mst_cost += weight  # Add the edge's weight to the total cost
                edges_used += 1  # Increment the count of edges used in the MST

                # If we've used enough edges to form a MST (Edges = Vertices - 1)
                if edges_used == totalVertices - 1:  
                    break  # Exit the loop early

        return mst_cost