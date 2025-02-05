import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stonesMaxHeap = []

        # Create a max heap by converting positive integers to negative
        # This is a work-around in python
        while len(stones):
            heapq.heappush(stonesMaxHeap, stones.pop() * -1)

        # We will always be able to smash 2 stones together
        # So we stop looping if we only have 1 stone left
        while len(stonesMaxHeap) > 1:
            # The first stone is most likely going to be larger than the 2nd stone
            # Max heap pop always grabs largest number first
            firstStone = heapq.heappop(stonesMaxHeap) * -1
            secondStone = heapq.heappop(stonesMaxHeap) * -1

            # If the first and second stone are equal it gets destroyed so we do nothing as its been heap popped already

            # But if they dont equal it means that 1st stone > 2nd stone, since 1st stone always bigger
            if firstStone != secondStone:
                # Subtract 1st stone with 2nd stone to get remainder stone and convert to negative
                heapq.heappush(stonesMaxHeap, (firstStone-secondStone) * -1)
        
        # Return the last value in the heap if there was a remainder stone
        if len(stonesMaxHeap) > 0: 
            return heapq.heappop(stonesMaxHeap) * -1
        
        # Return 0 if there were no remainder stones
        return 0

class CleanerSolution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []

        # Create a max heap by multiplying each number by -1
        for stone in stones:
            heapq.heappush(maxHeap, stone * -1)
        
        while(len(maxHeap) > 1):
            # Pop the 2 stones
            x = heapq.heappop(maxHeap) * -1 
            y = heapq.heappop(maxHeap) * -1

            # Only calculate if x does not equal y, if they equal each other they have already been popped thus destroyed
            if x != y:
                # subtract x - y since x is the larger stone due to being popped first
                heapq.heappush(maxHeap, (x-y) * -1)
            
        return maxHeap[0] * -1 if len(maxHeap) > 0 else 0