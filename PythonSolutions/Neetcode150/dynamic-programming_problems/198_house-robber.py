"""
- Adjacent numbers cannot be robbed (houses beside each other)
- nums array can be a length of 1
- nums is positive from 0 - 400
- return: max money that can be robbed without alerting police

State: dp[i] where i is the house index, and dp[i] represents the max cost at that house

Base Cases:
1. dp[0] = nums[0], first house can be robbed
2. dp[1] = max(nums[0], nums[1]), can't rob adjacent houses, so we can only select one of them

Recurrence Relation: At each step i, we can only take with us the max of current house and previous non-adjacent house or previous house.
- nums[i] + dp[i-2], can take current house + previous non adjacent house max costs
- dp[i-1], OR take the previous house
Transition: max(nums[i] + dp[i-2], dp[i-1])

Returns: dp[-1], last cost accumulated would be the max cost we can get
"""
class NonOptimizedBottomUpSolution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # If there are only 2 houses, return the max of the array
        if n <= 2:
            return max(nums)
        
        # Initialize dp array
            # State: i is the house index, value[i] is the max cost for the current house
        value = [0] * n
        # Base cases:
            # - Can only get value of first house when robbing first house 
            # - Cannot rob adjacent houses so we can only take 1 of the first 2 houses
        value[0] = nums[0]
        value[1] = max(nums[0], nums[1])

        # Recurrence relation: At each step i, can only take the max cost of previous non-adjacent houses
        for i in range(2, n):
            # Transition: Max between non-adjacent houses cost OR just the previous house 
            value[i] = max(nums[i] + value[i-2], value[i-1])

        # Return: The last accumulated max cost that was robbed
        return value[-1]
        
        

class BottomUpSolution:
    def rob(self, nums: List[int]) -> int:
        # If the list is empty, there's nothing to rob.
        if not nums: 
            return 0
        # If there are 1 or 2 houses, simply return the maximum value
        # available, since you can only choose from these without any
        # adjacent restrictions.
        elif len(nums) <= 2:
            return max(nums)

        # Initialize two variables to store the maximum amount of money
        # that can be robbed up to the previous house considering adjacency
        # (prevAdj) and the house before that (prevNonAdj).
        prevAdj, prevNonAdj = max(nums[0], nums[1]), nums[0]

        # Start looping from the third house (index 2) onwards.
        for i in range(2, len(nums)):
            # Calculate the current maximum amount that can be robbed.
            # It's either robbing the current house plus the amount from
            # two houses ago (for non-adjacency) or the amount from the
            # previous step (maintaining adjacency restrictions).
            currentMax = max(nums[i] + prevNonAdj, prevAdj)
            
            # Update our two tracking variables for the next iteration.
            # The current maximum becomes the new prevAdj (since we're
            # moving to the next house), and the previous prevAdj becomes
            # the new prevNonAdj (as it's now two steps back).
            prevAdj, prevNonAdj = currentMax, prevAdj
        
        # After going through all the houses, prevAdj holds the maximum
        # amount of money that can be robbed considering the adjacency
        # constraint.
        return prevAdj

class TopDownSolution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        # State: house, current house we are at that we can possibly rob
        def dfs(house):
            # Base case 1: Cost is already cached
            if house in cache:
                return cache[house]

            # Base case 2: No more houses left to rob
            if house < 0:
                return 0
            
            # Base case 3: First house, the only house that can current be robbed 
            if house == 0:
                return nums[house]

            # Base case 4: Second house, can either rob first or this house (can't rob adjacent houses)
            if house == 1:
                return max(nums[house], nums[0])
            
            # Recurrence Relation: Can take either the non-adjacent houses or the previous adjacent house
            cache[house] = max(nums[house] + dfs(house-2), dfs(house-1))

            return cache[house]
        
        # Passes in length of nums - 1 since nums is 0-indexed base
            # Runs DFS on last house which has the accumulation max cost of all previous houses
        return dfs(len(nums) - 1)

class NonOptimizedSolution:
    def rob(nums):
    # Recursive function to calculate the maximum amount
        def robFrom(i):
            # Base case: when there are no more houses left to consider
            if i >= len(nums):
                return 0
            # Recur by choosing to rob current house and skip next, or skip current house
                # robFrom(i + 1), "If I don't rob this house, what's the max I can get starting from the next house?"
                # robFrom(i + 2), "If I rob this house, what's the max I can get from the rest of the houses starting two steps ahead, since I can't rob the next one?"
            return max(nums[i] + robFrom(i + 2), robFrom(i + 1))
    
        # Start the recursion from the first house
        return robFrom(0)
