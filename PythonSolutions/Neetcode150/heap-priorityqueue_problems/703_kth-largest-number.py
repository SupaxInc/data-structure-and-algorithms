import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)

        # We want the heap to only have kth size
        # This allows us to return the kth largest element at the top of the min heap
            # Since its a min heap, the values that are left after popping are the largest
            # Therefore, the next pop will be the kth largest
        while len(self.minHeap) > self.k:
            print(heapq.heappop(self.minHeap))
        
        print(self.minHeap)

    def add(self, val: int) -> int:
        # Add the value to the heap
        heapq.heappush(self.minHeap, val)

        # Edge case, need to pop heap again once since its now greater than kth size after pushing new value
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        # The top of the heap is always accessed by index 0
        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)