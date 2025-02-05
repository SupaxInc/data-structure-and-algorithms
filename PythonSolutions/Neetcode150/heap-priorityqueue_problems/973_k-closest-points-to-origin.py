class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        # First calculate the euclidean distance to find which points are closest to origin
            # The euclidean distance tells us the value that is smallest is closer to the origin
        for point in points:
            x = point[0]
            y = point[1]
            # For euclidean distance calculation, we need to subtract the points with the origin
            # Since the origin is 0,0, we don't need to subtract the points to see how far it is since its 0
            # We just need to square it
            # E.g. point = [1,3], sqrt((1-0)^2 + (3-0)^2) = sqrt((1) + (9)) = sqrt(10)
            # NOTE: No need to sqrt since the largest value is always bigger than the smallest value regardless of sqrt
            heapq.heappush(minHeap, ((x**2)+(y**2), x, y))
        
        res = []
        for i in range(k):
            # Get the smallest value
                # When you pop a tuple from heap, it uses the first index in tuple
            val, x, y = heapq.heappop(minHeap)
            res.append([x, y])
        
        return res