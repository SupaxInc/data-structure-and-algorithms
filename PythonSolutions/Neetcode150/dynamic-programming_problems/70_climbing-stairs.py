class BruteForceSolution:
    def climb_stairs_dfs(n):
        # Base case: when n is 0 or 1, there is only one way to climb the stairs (either you're already there, or you take one step).
        if n <= 1:
            return 1
        
        # Recursive case: the number of ways to climb to step n is the sum of the ways to climb to step n-1 and to step n-2.
        # This is because at step n-1, you can take a single step to reach n, and at step n-2, you can take a double step to reach n.
        return climb_stairs_dfs(n-1) + climb_stairs_dfs(n-2)