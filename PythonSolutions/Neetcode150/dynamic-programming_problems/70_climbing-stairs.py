"""
- Positive numbers, n > 0

Example:
n = 2:
n = 0, There is 1 way to reach 0 steps which is not taking a step at all
n = 1, There is 1 way to reach 1 step whihch is to take 1 step
n = 2, 2 ways, 1 step + 1 step, 2 steps 

State: Our state will be dp[i] = number of distinct ways to reach step i

Recurrence Relation:
- To get all possible steps to get to step 3 you need,
    - dp[i-1], all possibilities from previous step
    - dp[i-2], all possibilities from 2 steps ago

Base Cases:
- dp[0] = 1 (1 way to reach step 0)
- dp[1] = 1 (1 way to reach step 1)
"""
class BottomUpSolution:
    def climbStairs(self, n: int) -> int:
        # If steps are 0 or 1, then only 1 way to climb
        if n <= 1:
            return 1

        # State: steps[i] is numbers of distinct ways to reach step i
            # - Initialize steps array
        steps = [0] * (n + 1)

        # Base cases:
            # steps[0] = 1, steps[1] (1 way to reach step 0 and step 1)
        steps[0] = 1
        steps[1] = 1

        # Begin recurrence relation: Begin at step 2 since step 0 and 1 are already 1
        for i in range(2, n+1):
            # Transition: 
                # Add all possibilities to reach step i using previous step answers
                # - steps[i-1] -> All possibilities from previous step
                # - steps[i-2] -> All possibilities from two steps ago
            steps[i] = steps[i-1] + steps[i-2]

        # Return the last in the array which is all of the possibilities from all steps until the last step
        return steps[n]

class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        
        # States:
            # - step, the number of distinct way to reach the current step
        def dfs(step):
            # Base case 1: The step is already in the cache
            if step in cache:
                return cache[step]
            
            # Base cases 2: Step 0 or 1 have 1 way to get to it
            if step <= 1:
                return 1
            
            # Recurrence relation: To get all possibilities for current step add possibilities of the previous steps:
                # step-1, all possibilities from previous step
                # step-2, all possibiliities from previous 2 steps
            cache[step] = dfs(step-1) + dfs(step-2)

            return cache[step]

        return dfs(n)


class BruteForceSolution:
    def climb_stairs_dfs(n):
        # Base case: when n is 0 or 1, there is only one way to climb the stairs (either you're already there, or you take one step).
        if n <= 1:
            return 1
        
        # Recursive case: the number of ways to climb to step n is the sum of the ways to climb to step n-1 and to step n-2.
        # This is because at step n-1, you can take a single step to reach n, and at step n-2, you can take a double step to reach n.
        return climb_stairs_dfs(n-1) + climb_stairs_dfs(n-2)