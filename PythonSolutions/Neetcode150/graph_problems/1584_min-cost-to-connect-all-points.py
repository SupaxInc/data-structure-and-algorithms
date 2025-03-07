class PrimSolution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # *This problem is a COMPLETE graph*
            # Meaning that all points can connect with each other
            # Therefore, we are not limited only to the vertices that we have visited
            # We can actually visit any vertex that we want
        totalVertices = len(points)
        visited = set()
        cost = 0

        # Typically in prim's algorithm, you want to start at point 0 but this can be a random point
        minHeap = [(0, 0)] # (current cost, current point)

        # Calculate the manhattan distance between two points (x1 - x2) + (y1 - y2)
        # This will be used as the cost of the points
        def manhattan(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1]-points[j][1])

        # Stop the BFS when we hit E = V - 1
        while len(visited) < totalVertices:
            # Get the lowest cost point in heap
            currCost, currPoint = heapq.heappop(minHeap)

            # Even though we only explore vertices that have not been visited (see exploration below)
            # There is still a chance that a vertex has been visited since we are randomly popping from a min heap
            if currPoint in visited:
                continue

            # Visit the vertex
            cost += currCost
            visited.add(currPoint)

            # Explore ALL the vertices and calculate ALL of the cost for each vertices
                # It is a COMPLETE graph we can visit any vertex
                # neiPoint is an index in the points list which matches to a vertex
                # e.g. points = [[0,0],[2,2]], neiPoint = 1 is vertex 1 which is point [2, 2]
            for neiPoint in range(totalVertices):
                # Only explore the and calculate the cost of the points that have not been visited
                if neiPoint not in visited:
                    heapq.heappush(minHeap, (manhattan(currPoint, neiPoint), neiPoint))

        return cost
    

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
            # i+1 since we need to compare i (x1, y1) with every other j (x2, y2), generating all possible edges for each point
            for j in range(i + 1, totalVertices):
                # Manhattan distance: (x1 - x2) + (y1 - y2)
                weight = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((weight, i, j))

        # Sort edges by weight
            # Allows us to select and connect the most minimum weights first for each point (weight, x, y)
        edges.sort()

        # Kruskal's algorithm to form MST
        uf = UnionFind(totalVertices)
        mst_cost = 0  # Total cost of the MST
        edges_used = 0  # Number of edges added to the MST

        for weight, u, v in edges:
            # Add edges 1 by 1, connecting points (u, v) together to form a graph
                # Check if it doesn't form a cycle
            if uf.union(u, v):  
                mst_cost += weight  # Add the edge's weight to the total cost
                edges_used += 1  # Increment the count of edges used in the MST

                # If we've used enough edges to form a MST (Edges = Vertices - 1)
                if edges_used == totalVertices - 1:  
                    break  # Exit the loop early

        return mst_cost