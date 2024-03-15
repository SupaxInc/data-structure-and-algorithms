class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        for x, y in points:
            # Calculate the Euclidean distance
                # Square root does not matter since the highest number has a higher sqrt anyways
            minHeap.append((x**2 + y**2, x, y))
        
        # Heapify will only sort using the first value in a tuple
        heapq.heapify(minHeap)

        for _ in range(k):
            # Destruct the tuple
            val, x, y = heapq.heappop(minHeap)
            # Append only coordinates
            res.append([x, y])
        
        return res
