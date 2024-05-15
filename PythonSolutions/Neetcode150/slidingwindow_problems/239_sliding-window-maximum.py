class BruteForceSolution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        for i in range(len(nums)): 
            if i + k <= len(nums):
                maxHeap = [-num for num in nums[i:i+k]]
                heapq.heapify(maxHeap)
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
                # q[0] is accessing the index NOT the value of the queue
                # It is the index of the first element added to queue
            if q and q[0] < start:
                q.popleft() # Remove first element added to queue
            
            # Maintain descending order in current fixed window
                # Compares last element added to queue with current element
            while q and nums[q[-1]] < nums[end]:
                q.pop() # Remove last element added to queue
            # E.g. [7, 6] -> current element is 9 -> so [9] will just be left after comparison
            
            q.append(end) # Add the current index to queue after maintaining descending order

            # If the window is of valid size then add to result
            if (end - start + 1) == k:
                # Add the first element in queue (the max since its descending order)
                res.append(nums[q[0]])
                start += 1 # Move start forward
        
        return res