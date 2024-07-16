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