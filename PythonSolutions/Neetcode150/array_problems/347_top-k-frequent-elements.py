class OptimizedSolution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        maxHeap = []
        count = defaultdict(int) # Create a dictionary with a key of int

        for num in nums:
            count[num] += 1 # Defaultdict allows us to not have to check if key exists
        
        for key, val in count.items():
            # Push a tuple to the heap
            # A heap will use the first value of an array to add to the top of the heap
            # Need to multiply by -1 since Python heap is only a min heap
            maxHeap.append((val * -1, key))
        
        # Turn the maxHeap array into a heap in O(n) time
        # It will use the first index of the tuples in the array to sort the heap
        heapq.heapify(maxHeap)

        for i in range(0, k): # O(k)
            # Append the 2nd value of the tuple to the result array, this will be the element
            res.append(heapq.heappop(maxHeap)[1]) # Insert or popping from heap is O(log n) time
        
        # Worst case time complexity: O(k * n)
            
        return res

class MoreOptimizedSolution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        # Create a bucket based on length of nums array
        # An element can only show length(nums) of times
        bucket = [[] for _ in range(len(nums)+1)] 
        res = []

        # Create a frequency map
        for num in nums:
            count[num] += 1

        # The index will be used as the count
        # The value will be an array of elements since elements could show up same amount of times
        for key, val in count.items():
            bucket[val].append(key)
    
        # Iterate backwards to get the most found elements
        for i in range(len(bucket)-1, -1, -1): # O(n)
            for number in bucket[i]: # O(k)
                if len(res) < k:
                    res.append(number)
        
        return res