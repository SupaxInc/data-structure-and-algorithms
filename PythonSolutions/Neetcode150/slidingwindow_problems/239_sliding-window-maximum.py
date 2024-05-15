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
