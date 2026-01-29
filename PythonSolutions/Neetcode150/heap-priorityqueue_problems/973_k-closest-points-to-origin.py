from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        minHeap = []

        # Calculate euclidean distance between point of origin and a point
        for x, y in points:
            # Since point of origin is (0, 0), calculations become: sqrt(x^2 + y^2) since other coords are just 0
            heapq.heappush(minHeap, [(x**2 + y**2), x, y])
        
        for _ in range(k):
            # Pop from min heap in range of K, giving us the most min value per iteration
            _, x, y = heapq.heappop(minHeap)
            res.append([x, y])
        
        return res
        
