class Solution:
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

class NonOptimizedSolution:
    def rob(nums):
    # Recursive function to calculate the maximum amount
        def robFrom(i):
            # Base case: when there are no more houses left to consider
            if i >= len(nums):
                return 0
            # Recur by choosing to rob current house and skip next, or skip current house
            return max(nums[i] + robFrom(i + 2), robFrom(i + 1))
    
        # Start the recursion from the first house
        return robFrom(0)
