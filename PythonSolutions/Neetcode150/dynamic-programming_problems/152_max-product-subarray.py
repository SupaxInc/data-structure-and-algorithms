"""
- subarray that contains max product
- length of nums array 1 to 2 * 10^4
- nums[i] can be between -10 to 10
- RETURNS: max product, guaranted to fit in a 32 bit integer
- can't use sliding window, too many possibilities
- double negatives can make positives

State: dp[i], i is current digit, and dp[i] represents max product seen so far
- problem here is we need to track the most min product in the case that a double negative shows up
- so track 2 states:
    - maxProduct[i] -> highest max product seen so far in a subarray
    - minProduct[i] -> used as a helper to select a subarray with the most negative product to be used by max product

Transitions:
1. maxProduct[i] = max(nums[i], maxProduct[i-1] * nums[i], minProduct[i-1] * nums[i])
    - nums[i] -> start a NEW subarray starting at current num
    - maxProduct[i-1] * nums[i] -> CONTINUE max product subarray seen previously, including current number
    - minProduct[i-1] * nums[i] -> CONTINUE min product subarray seen previously, including current number
                    - Uses the min product as its possible that current number is NEGATIVE creating a larger number
2. minProduct[i] = min(nums[i], maxProducct[i-1] * nums[i], minProduct[i-1] * nums[i])
    - nums[i] -> start a NEW MIN subarray starting at current num
    - maxProduct[i-1] * nums[i] -> possible that previous subarray for max product has become a larger negative
    - minProduct[i-1] * nums[i] -> possible that current min subarray has become a larger negative

NOTE: The idea, we are just constantly flipping between max and min prod state subarrays OR starting anew.

3. max(maxProduct[i], max)
    - final max will always be checking for the maxProduct since ultimately minProduct is just a helper
    - maxProduct always uses minProduct in its calculations to handle negatives


Base cases: Best max or min product at the beginning will always be the first number
1. currentMax = nums[0]
2. maxProduct[0], minProduct[0] = nums[0], nums[0]

Returns: currentMax
"""
class NonOptimizedSolution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        # State 1: maxProd[i], highest product seen so far in a subarray
        maxProd = [0] * (n)
        # State 2: minProd[i], used as a helper to track most negative product seen so far to be used by max product
        minProd = [0] * (n)

        # Base cases: Max and min product at the beginning will always be the first number
        globalMax = nums[0]
        maxProd[0], minProd[0] = nums[0], nums[0]

        # Recurrence relation: At each number i, find the max product seen so far
        for i in range(1, n):
            # Transition 1: Find which subarray to continue from that has the HIGHEST product
                # nums[i]                -> start a new subarray at current index
                # maxProd[i-1] * nums[i] -> continue position from previous max subarray
                # minProd[i-1] * nums[i] -> change to use previous min subarray as its now larger (maybe flipped thru negatives)
            maxProd[i] = max(nums[i], maxProd[i-1] * nums[i], minProd[i-1] * nums[i])

            # Transition 2: Find which subarray to cocntinue from that has the LOWEST product
                # nums[i]                -> start a new lower product subarray at current index
                # maxProd[i-1] * nums[i] -> continue from previous max subarray as it may have been flipped thru negatives
                # minProd[i-1] * nums[i] -> check if current min subarray is still smaller than the rest
            minProd[i] = min(nums[i], maxProd[i-1] * nums[i], minProd[i-1] * nums[i])

            # Global max now changes depending on the MAX product subarray, final answer will always be the max product
                # minProd is just a helper state for maxProd in the case that a double negative occurs
                # Prevents us from just greedily always choosing the positives as negatives may become larger
            globalMax = max(globalMax, maxProd[i])
        
        return globalMax
    
class OptimizedSolution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # At this point, min and max is the first number
        # max_product tracks the maximum product ending at the current position.
        # min_product tracks the minimum product ending at the current position.
            # Important to track both as a negative number could turn the minimum product into a maximum.
        minProd = maxProd = result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            # Swap min and max when num is negative because multiplying two negatives can result in a max.
            if num < 0:
                maxProd, minProd = minProd, maxProd
            
            # IF at any point the min or max selects the current number
                # This means we have resetted the subarray to current position
            maxProd = max(num, maxProd * num)
            minProd = min(num, minProd * num)

            result = max(maxProd, result)
        
        return result