class BottomUpSolution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costLength = len(cost)
        if costLength < 2: # If there is only 1 step, then just return the 1st step
            return cost[0]
        
        mccs = [1] * costLength # Create an array of 1's based on length of cost array

        mccs[0], mccs[1] = cost[0], cost[1] # Base cases

        for i in range(2, len(mccs)): 
            mccs[i] = cost[i] + min(mccs[i-1], mccs[i-2]) # Recurrence relation formula
        
        # Return the last 2 steps since it has cumulative min cost was between the 2 steps
            # and we can take the 2nd last step or the 1st step to reach the end.
        return min(mccs[-1], mccs[-2])