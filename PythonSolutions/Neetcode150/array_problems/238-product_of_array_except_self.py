from typing import List
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
        n = len(nums)
        if n < 2:
            return []
        
        # Initialize size of result with any value
        res = [1] * n

        # Calculate prefix, begin with a 1
        prefixProduct = 1
        for i in range(n):
            #* No need to multiply here
            res[i] = prefixProduct
            prefixProduct *= nums[i]

        # Calculate postfix by reversing prefixes, begin with a 1
        postfixProduct = 1
        for i in range(n-1, -1, -1):
            #* Do not use nums[i], use the current prefixes (res[i]) to get the cross multiplication between prefix and postfix
            res[i] *= postfixProduct
            postfixProduct *= nums[i]

        return res