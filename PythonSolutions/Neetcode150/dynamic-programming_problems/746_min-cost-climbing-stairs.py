"""
- Cost is positive only 0 - 999
- Cost length can be from 2 - 1000

State: dp[i], where i is step, therefore, dp[i] represents the minimum cost to reach step i

Base cases: We can either take take 1st step or jump to 2nd step right away
- dp[0] = costs[0], most min cost for 1st step is the cost of the 1st step
- dp[1] = costs[1], most min cost for 2nd step is the cost of the 2nd step

Recurrence Relation: At each step i, we can arrive from either step i-1 or i-2
There will be the use of 2 possibilities,
- dp[i-1], the min cost of all possibilities for previous step
- dp[i-2], the min cost of all possibilities for 2 steps ago
- min(dp[i-1], dp[i-2]), for current step i we need to select the most min between the 2 steps
- cost[i], cost of current step to add for current step possibility
Transition: dp[i] = min(dp[i-2], dp[i-1]) + costs[i]

Returns: Either the last step or 2nd last step since we can jump from 2nd last step
"""
class BottomUpSolution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # State: minCosts[i], where i is step, and minCosts[i] represents the min cost to reach step i
        minCosts = [0] * len(cost)

        # Base cases: We can either take the 1st or 2nd step right away
            # dp[0] = cost[0], cost of 1st step
            # dp[1] = cost[1], cost of 2nd step
        minCosts[0] = cost[0]
        minCosts[1] = cost[1]

        # Recurrence relation: The current min costs i including all possibilities of previous 2 steps
        for i in range(2, len(cost)):
            # Transition: Find min of all min cost possibilities of the past 2 steps and add the current step cost
            minCosts[i] = min(minCosts[i-1], minCosts[i-2]) + cost[i]

        # Returns either the last step or 2nd last step since we can jump from 2nd last step
        return min(minCosts[-1], minCosts[-2])
    
class TopDownSolution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}

        # States:
            # step, represents the current step we are on that contains a min cost
        def dfs(step):
            # Base case 1: Step already exists in cache
            if step in cache:
                return cache[step]
            
            # Base case 2: We can either take step 0 or step 1 at the beginning
            if step < 2:
                return cost[step]
            
            # Recurrence relation: At each step i, we can arrive from either step-1 or step-2
            cache[step] = min(dfs(step-1), dfs(step-2)) + cost[step]

            return cache[step]
        
        costLength = len(cost)
        # The goal is to reach the top (position n, which is beyond the last element)
        # We can reach the top from either:
            # 1. The last step (costLength-1) by taking 1 more step
            # 2. The second-to-last step (costLength-2) by taking a 2-step jump
        # We take the minimum of these two options to find the overall minimum cost
        return min(dfs(costLength-1), dfs(costLength-2))