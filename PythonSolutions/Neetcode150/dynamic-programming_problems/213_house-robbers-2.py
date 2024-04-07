class BottomUpOptimizedSolution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(sub_nums):
            if len(sub_nums) <= 2:
                return max(sub_nums)
            
            prevNonAdj, prevAdj = sub_nums[0], max(sub_nums[0], sub_nums[1])

            for i in range(2, len(sub_nums)):
                currentMax = max(sub_nums[i] + prevNonAdj, prevAdj)
                prevNonAdj = prevAdj
                prevAdj = currentMax
            
            return prevAdj
                
        if not nums:
            return 0
        elif len(nums) <= 1:
            return nums[0]
        # Rob houses without 1st element and last element
        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))


class BottomUpNonOptimizedSolution:
    def rob(nums):
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        
        # Helper function to rob houses in a linear fashion
        def rob_linear(houses):
            if len(houses) == 0:
                return 0
            if len(houses) == 1:
                return houses[0]
            
            dp = [0] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            for i in range(2, len(houses)):
                dp[i] = max(dp[i-1], dp[i-2] + houses[i])
            return dp[-1]
        
        # Exclude the first house and exclude the last house, then take the max
        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))
