# Similar to sorting algorithm since heappush is O(log n)
class NotOptimizedSolution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []

        for num in nums: # O(n log n)
            heapq.heappush(maxHeap, num * -1)
        
        for i in range(0, k): # O(k log n)
            kthLargest = heapq.heappop(maxHeap) * -1
            if i == k-1:
                return kthLargest
        
        return 0
    
class BetterOptimizedSolution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Min heap of size k, helps us return the Kth largest element
        # since we can get the root of the heap minHeap[0] which is the Kth number
        minHeap = nums[:k]
        heapq.heapify(minHeap)

        # Start comparing against all nums starting from index k
        for num in nums[k:]:
            if num > minHeap[0]:
                # Heap push pop, will push to heap then pop
                # Helps sort the heap to get the kth largest
                heapq.heappushpop(minHeap, num)
        
        # Root of min heap will be kth largest element since its of size k
        return minHeap[0]



