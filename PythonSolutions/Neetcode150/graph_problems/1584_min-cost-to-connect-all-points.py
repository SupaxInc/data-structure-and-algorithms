class PrimSolution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # *This problem is a COMPLETE graph*
            # Meaning that all points can connect with each other
            # Therefore, we are not limited only to the vertices that we have visited
                # Not like exploring with graph[neiPoint] instead visiting all vertices with range(totalVertices)
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
                # Only explore and calculate the cost of the points that have not been visited
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

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False
        
        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        elif self.rank[rootY] > self.rank[rootX]:
            self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1
        
        return True

class UnionFindSolution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Each point is a vertex on the complete graph
        totalVertices = len(points)

        # Create the complete edge list that includes the cost (manhattan distance)
        edges = []
        for i in range(totalVertices):
            # Need to compare i (x[i], y[i]) with every j (x[j], y[j]) to get all cost for each i'th point
            for j in range(i + 1, totalVertices):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((cost, i, j)) # (cost, curr point, next point)
        
        # Need to sort the edge list by cost to get the most minimum costs first
        edges.sort()

        # Begin joining the edge list
        uf = UnionFind(totalVertices)
        totalCost = 0
        edgesUsed = 0

        for cost, curr, to in edges:
            # Check if we can join the edges without forming a cycle
            if uf.union(curr, to):
                totalCost += cost
                edgesUsed += 1

                # Stop joining edges when we've reached E = V - 1
                if edgesUsed == totalVertices - 1:
                    return totalCost
        
        return totalCost