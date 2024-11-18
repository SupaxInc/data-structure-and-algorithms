class MySolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return []
        
        numsLength = len(nums)
        res = []

        # Prefix is product starting from left
        prefix = [nums[0]] # Add first value of nums to prefix
        
        # Postfix is product starting from right
        postfix = [0] * numsLength
        postfix[-1] = nums[-1] # Add last value of nums to postfix

        # Compute the prefix product
            # Start from index 1 so we can compute the product of previous numbers
        for i in range(1, numsLength):
            prefix.append(prefix[i-1] * nums[i])
        
        # Compute the postfix product
            # Start from the 2nd last index to compute previous numbers
        for i in range(numsLength - 2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i]
        
        # For each index i:
            # prefix[i-1] contains product of all elements to the left of i
            # postfix[i+1] contains product of all elements to the right of i
            # Therefore, we are effectively skipping the product of nums[i] (current element we are on)
        for i in range(len(nums)):
            if i - 1 < 0: 
                # Multiply by 1 if we are at the first element so we don't multiply results by 0
                res.append(1 * postfix[i+1])
            elif i + 1 >= numsLength: 
                # Multiply by 1 if we are at the last element so we don't multiply results by 0
                res.append(1 * prefix[i-1])
            else: 
                # Multiply the prefix and postfix products to get product of all elements except nums[i]
                # **Effectively creating a product of array except self**
                res.append(prefix[i-1] * postfix[i+1])
        
        return res

class BetterSpaceSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Check for edge cases
        if len(nums) < 2:
            return []
        
        n = len(nums)
        res = [1] * n  # Initialize the result array with 1's

        # Compute prefix products directly into result array
        prefix_product = 1 # Begin with 1 to get the product before index 0 and prevents multiplying by 0
        for i in range(n):
            res[i] = prefix_product
            prefix_product *= nums[i] # Accumulate the product of all elements to the left of i
        
        # ** The result array now contains the prefix products, begin computing postfix products **
        # Compute postfix products directly into the result array
        postfix_product = 1 # Begin with 1 to get the product after index length of nums and prevents multiplying by 0
        for i in range(n-1, -1, -1):
            res[i] *= postfix_product
            postfix_product *= nums[i] # Accumulate the product of all elements to the right of i
        
        return res