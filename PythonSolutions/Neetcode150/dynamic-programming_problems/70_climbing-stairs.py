class BottomUpSolution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1 # There's only one way to climb 0 or 1 stair.

        result = [1, 1] # Base cases: 1 way to climb 0 and 1 stairs.

        for i in range(2, n + 1): # Start from 2 as we already know the first two cases. n+1 is similar to i <= n in Python
            result.append(result[i-1] + result[i-2])
        
        return result.pop() # Return the last element in the list which corresponds to `n` stairs.

class TopDownSolution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def dfs(n):
            if n in cache:
                return cache[n]
            else:
                if n <= 1:
                    return 1 # Return 1 at 0 or 1 steps because there is 1 way to do something at 0 steps.
                
                cache[n] = dfs(n-1) + dfs(n-2)
                return cache[n]
        
        return dfs(n)


class BruteForceSolution:
    def climb_stairs_dfs(n):
        # Base case: when n is 0 or 1, there is only one way to climb the stairs (either you're already there, or you take one step).
        if n <= 1:
            return 1
        
        # Recursive case: the number of ways to climb to step n is the sum of the ways to climb to step n-1 and to step n-2.
        # This is because at step n-1, you can take a single step to reach n, and at step n-2, you can take a double step to reach n.
        return climb_stairs_dfs(n-1) + climb_stairs_dfs(n-2)