class MedianFinder:

    def __init__(self):
        self.smallerNums = [] # Max heap
        self.largerNums = [] # Min heap

    def addNum(self, num: int) -> None:
        # Add to smaller nums first
            # Then begin checking if the current num is smaller than root of max heap (largest num in smaller nums)
        if len(self.smallerNums) == 0 or num <= (self.smallerNums[0] * -1):
            heapq.heappush(self.smallerNums, num * -1)
        # Add to larger numbers if current num is greater than largest num in smaller nums
        else:
            heapq.heappush(self.largerNums, num)
        
        # Begin balancing the heap if there are differences of 2
            # If there is a difference of 2 we cant find the median properly
        if len(self.smallerNums) - len(self.largerNums) > 1:
            # Push the largest num in smaller nums (max heap) to larger nums (min heap)
            heapq.heappush(self.largerNums, heapq.heappop(self.smallerNums) * -1)
        elif len(self.largerNums) - len(self.smallerNums) > 1:
            heapq.heappush(self.smallerNums, heapq.heappop(self.largerNums) * -1)

    def findMedian(self) -> float:
        # At this point, there could only be a difference of 1 or it equals

        # If there is a difference of 1 return the root of the heap with the larger difference
        if len(self.smallerNums) > len(self.largerNums):
            return self.smallerNums[0] * -1
        elif len(self.largerNums) > len(self.smallerNums):
            return self.largerNums[0]
        
        # Else, if there are no differences, get the median by getting the average of the largest roots of both heaps
        return ((self.smallerNums[0] * -1) + self.largerNums[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()