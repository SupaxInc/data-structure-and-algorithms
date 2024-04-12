class Solution:
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