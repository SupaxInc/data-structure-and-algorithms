class MySolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return []
        
        res = []
        numsLength = len(nums)
        prefix = [nums[0]]
        postfix = [0] * numsLength
        postfix[-1] = nums[-1]

        for i in range(1, numsLength):
            prefix.append(prefix[i-1]*nums[i])
        
        for i in range(numsLength-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i]

        for i in range(0, numsLength):
            if i - 1 < 0:
                res.append(1 * postfix[i+1])
            elif i + 1 >= numsLength:
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

        # Compute prefix products
        prefix_product = 1
        for i in range(n):
            res[i] = prefix_product
            prefix_product *= nums[i]
        
        # Compute postfix products directly into the result array
        postfix_product = 1
        for i in range(n-1, -1, -1):
            res[i] *= postfix_product
            postfix_product *= nums[i]
        
        return res