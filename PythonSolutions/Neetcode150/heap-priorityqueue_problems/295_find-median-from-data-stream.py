class MedianFinder:

    def __init__(self):
        # Need to get the largest of the smaller numbers
        self.smallerNumbers = [] # Max heap
        # Need to get the smallest of the larger numbers
        self.largerNumbers = [] # Min heap

        # Helps find the median easier by:
            # Knowing what is the mid number or the two middle numbers 

    def addNum(self, num: int) -> None:
        # * A) Add the current numbers to the heaps *

        # Add to smaller number MAX heap if:
            # The max heap is empty or
            # The current number is less than or equal to the largest SMALLEST number
        # Handles both first function call and later calls
        if len(self.smallerNumbers) == 0 or num <= (self.smallerNumbers[0] * -1):
            heapq.heappush(self.smallerNumbers, num * -1)
        else:
            heapq.heappush(self.largerNumbers, num)
        
        # * B) Balance the heaps if the length difference between them is greater than 1 *
            # If there is a difference of 1+ then its harder to find the median
        
        # Add to larger number MIN heap if:
            # The smaller number MAX heap has more numbers than the MIN heap
        if (len(self.smallerNumbers) - len(self.largerNumbers)) > 1:
            heapq.heappush(self.largerNumbers, heapq.heappop(self.smallerNumbers)*-1)
        elif (len(self.largerNumbers) - len(self.smallerNumbers)) > 1:
            heapq.heappush(self.smallerNumbers, heapq.heappop(self.largerNumbers)*-1)

    def findMedian(self) -> float:
        # * A) Return the middle point as the median *
            # addNum function handles if there are differences of 2
        
        # If there is a difference of 1 then that means the larger length heap has the mid point:
            # Smaller numbers has the difference then return the largest SMALLEST number
            # Largest numbers has the difference then return the smallest LARGEST number
        if len(self.smallerNumbers) > len(self.largerNumbers):
            return self.smallerNumbers[0] * -1
        elif len(self.largerNumbers) > len(self.smallerNumbers):
            return self.largerNumbers[0]

        # * B) Return the two middle numbers / 2 as the median *
        return ((self.smallerNumbers[0] * -1) + self.largerNumbers[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()