class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        V = len(points)
        visited = set()

        # Beginning at point 0, so our cost is 0
        pq = [(0, 0)] # (cost, point #)

        def manhattan(i, j):
            # Manhattan distance: (x1 - x2) + (y1 - y2)
            return abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
        
        # Stop Prims algorithm when we have visited total amount of vertices
            # This will create an MST, since total vertices - 1 = total edges
        while len(visited) < V:
            currCost, currPoint = heapq.heappop(pq)
            # Undirected graph so there is chance we have already visited a point
            if currPoint in visited:
                continue
            
            # Visit the vertex
            visited.add(currPoint)
            res += currCost

            # Traverse all of the other points since the point can be a neighbour to all points
            for nextPoint in range(V):
                if nextPoint not in visited:
                    heapq.heappush(pq, (manhattan(currPoint, nextPoint), nextPoint))
        
        return res