class BruteForceSolution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        for i in range(len(nums)): 
            # Ensures that current fixed window of size k is not out of bounds
            if i + k <= len(nums):
                # Creates a max heap of the current fixed window
                maxHeap = [-num for num in nums[i:i+k]]
                heapq.heapify(maxHeap)
                # Appends the highest value of the current fixed window to result
                res.append(heapq.heappop(maxHeap) * -1)
            else:
                break
        
        return res

class OptimizedSolution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        q = deque()
        start = 0
        for end in range(len(nums)):
            # Remove elements that are not within the current fixed window
                # **q[0] grabs the value of the first element (in this case the index) added to the queue**
            if q and q[0] < start:
                q.popleft() # Remove first element added to the front of the queue
            
            # Maintain descending order in current fixed window by removing elements that are less than current element
                # **q[-1] grabs the value of the last element (in this case the index) added to the queue**
                # E.g. We want to add 9 to the queue [7, 6] -> current element is 9 -> so [9] will just be left after comparison
            while q and nums[q[-1]] < nums[end]:
                q.pop() # Remove last element that was added to the back of queue
                # After popping, we will have the index of the highest value in the current fixed window
            
            # **Here is where the index is being added to the queue**
            # Adds the current index which is the index of nums array that has the highest value in the current fixed window
            q.append(end)

            # If the window is of valid size then add the highest value of window to result
            if (end - start + 1) == k:
                # Add the first element in front of the queue (the max since its descending order)
                res.append(nums[q[0]])
                start += 1 # Move start forward
        
        return res