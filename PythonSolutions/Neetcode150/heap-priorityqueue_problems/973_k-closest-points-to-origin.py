class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        for x, y in points:
            # Calculate the Euclidean distance
                # Square root does not matter since the highest number has a higher sqrt anyways
                    # Just need to just get the coords with the power of 2 since the origin is just (0, 0), so rest of formula doesn't matter
                # Create a tuple of the (Euclidean distance calculation, x, y), helps us know what x,y coords were for the distance
            minHeap.append((x**2 + y**2, x, y))
        
        # Heapify will only sort using the first value in a tuple
            # IF there are duplicates then it uses the next value in the tuple
        heapq.heapify(minHeap)

        # The one closest to the origin is the smallest value in the heap
        for _ in range(k):
            # Destruct the tuple
            val, x, y = heapq.heappop(minHeap)
            # Append only coordinates
            res.append([x, y])
        
        return res
