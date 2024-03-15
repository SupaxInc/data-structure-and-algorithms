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


# O(n), O(n^2 worst case)
class QuickSelectRecursiveSolution:
    def partition(self, nums, low, high):
        # Prevents worst case scenario
        pivot = random.randint(low, high)
        nums[pivot], nums[high] = nums[high], nums[pivot]
        # After swap, pivot is now at nums[high]
        pivot = nums[high]
        i = low

        for j in range(low, high):
            # Check if the current number is less than our pivot point
            if nums[j] <= pivot:
                # Swap numbers to possible new i pivot point
                    # This allows us to make sure all numbers before our pivot point is less than it
                nums[i], nums[j] = nums[j], nums[i]
                # Increment index i so we can find our new pivot point
                i += 1
        
        # Swap new pivot point number to old pivot point number
        # All numbers before new pivot point are now less than it
        # And all numbers after new pivot point are greater than it
        nums[i], nums[high] = nums[high], nums[i]

        # Return the new pivot point
        return i


    def quickSelect(self, nums, low, high, k):
        if low <= high:
            pivotIndex = self.partition(nums, low, high)

            if pivotIndex == k:
                return nums[k]
            elif pivotIndex < k:
                return self.quickSelect(nums, pivotIndex + 1, high, k)
            else:
                return self.quickSelect(nums, low, pivotIndex - 1, k)


    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Edge case, if were trying to find a kth largest but the array isn't big enough
        if len(nums) < k:
            return None
        # Quick select, will sort it in descending order, so we need to subtract by k to get Kth largest
        k = len(nums) - k 

        return self.quickSelect(nums, 0, len(nums)-1, k)



# Solution: QuickSelect
# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n)
#   - Worst Case: O(n^2)
# Extra Space Complexity: O(1)
class QuickSelectIterativeSolution2:
    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot, fill = nums[right], left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[fill], nums[i] = nums[i], nums[fill]
                fill += 1

        nums[fill], nums[right] = nums[right], nums[fill]

        return fill

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        left, right = 0, len(nums) - 1

        # Very similar to binary search
        while left < right:
            pivot = self.partition(nums, left, right)

            if pivot < k:
                left = pivot + 1
            elif pivot > k:
                right = pivot - 1
            else:
                break

        return nums[k]

