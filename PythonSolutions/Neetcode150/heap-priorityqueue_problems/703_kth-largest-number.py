import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k, self.minHeap = k, nums
        heapq.heapify(self.minHeap)

        # Make the min heap size of Kth largest so its easier to know what the kth largest is
        while(len(self.minHeap) > self.k):
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Add the new value to the min heap
        heapq.heappush(self.minHeap, val)

        # Now that the min heap is larger than the length of Kth largest
        # Pop it so that we keep track of what the Kth largest is
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        # Since the min heap is again the size of kth largest, return the top of the heap (smallest value in the heap)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)