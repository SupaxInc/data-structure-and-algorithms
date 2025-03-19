"""
- length of nums 1 to 100
- positive numbers, 0 to 1000
- neighborhood is arranged in a circle, therefore, array is circular (house at beginning is neighbors with last house)
- adjacent houses can't be robbed (numbers next to each other)
- in this case we can just do 2 runs, 1 skipping last house, and 1 skipping first house

State: dp[i], i is house index, dp[i] represents max cost at that current accumulated from previous house selections

Base cases:
1. If len(nums) == 2, return 0, can't rob any houses
2. If len(nums) == 1, return nums[0], only have 1 house to rob
3. dp[0] = nums[0], we will be skipping first and last house, so do same house robber concept
4. dp[1] = max(nums[0], nums[1])

Recurrence relation: At each house i, get the max cost of current house plus previous max cost possibilities
Transition: max(nums[i] + dp[i-2], dp[i-1])

Returns: max(exclude first house, exclude last house)
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # After excluding first or last house, no need to rob circular, just rob it linearly
        def robLinear(houses):
            # If there are only 2 houses, return the house with highest value
            if len(houses) <= 2:
                return max(houses)
            
            # Initialize DP array
                # State: i is house index, dp[i] represents current cost including previous max cost possibilities
            dp = [0] * len(houses)
            # Base cases: Use either the 1st house or the max of the non adjacent houses
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            # Recurrence relation: At each house i, choose either the current house or the non adjacent houses
            for i in range(2, len(houses)):
                dp[i] = max(houses[i] + dp[i-2], dp[i-1])
            
            # Return the last value which is the accumulated max cost based on transitions
            return dp[-1]
        
        # Rob the houses twice:
            # 1. Including the first house [1:]
            # 2. Exclusing the last house [:-1], -1 will exclude the last house due to being non-exclusive
        # This prevents the circular array relationship and allows us to rob linearly
        return max(robLinear(nums[1:]), robLinear(nums[:-1]))
        

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
