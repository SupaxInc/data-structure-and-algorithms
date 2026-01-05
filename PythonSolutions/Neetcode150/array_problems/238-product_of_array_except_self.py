class ReadableSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)

        # Calculate prefix (left -> right)
            # Add the first num to prefix (first num is always going to be the same since we are multiplying by 1)
        prefix = [nums[0]]
        # Begin at 1 to skip first index, then begin getting the product prefixes
        for i in range(1, n):
            prefix.append(prefix[i-1] * nums[i])

        # Calculate postfix (right -> left)
            # Similarly to prefix, add the last num in the last index postfix
        postfix = [0] * n
        postfix[-1] = nums[-1]
        # Begin at the 2nd last index
        for i in range(n-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i]

        #* Remember:
            #* Prefix should contain a 1 at the beginning
            #* Postfix should contain a 1 at the end
        #* Since we aren't adding it to the arrays, we need to deal with it here
        
        # Get result by doing cross multiplication between prefix[i-1] * postfix[i+1]
            # First index: Since prefix[i-1] would be out bounds multiple by 1
            # Last index: Similarly postfix[i+1] be out of bounds so just multiply by 1
        for i in range(n):
            if i == 0:
                res.append(1 * postfix[i+1])
            elif i == n - 1:
                res.append(1 * prefix[i-1])
            else:
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