class MemoizedSolution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def dfs(row, col):
            # Base case: Boundary checks
            if row >= m or col >= n:
                return 0
            # Base case: End point
            if row == m - 1 and col == n - 1:
                return 1
            # Check if the key is in the cache
            if (row, col) in cache:
                return cache[(row, col)]

            # Recurrence relation
            cache[(row, col)] = dfs(row, col + 1) + dfs(row + 1, col)
            return cache[(row, col)]
        
        # The starting point of the cache would have all of the unique paths stored
        return dfs(0, 0)

class TopDownSolution:
    def uniquePaths(self, m: int, n: int) -> int:
        # The "bottom" row will all just have 1 unique path
        dp = [1] * n

        # Iterate through the array like its a 2d array
            # Pretend to flip the 2d grid upside down and invert it for bottom up approach
        for row in range(1, m): # Skip 1st row, all 1's
            for col in range(1, n): # Skip 1st col, all 1's
                # Look at the upside down inverted 2d grid here
                    # Adding the previous number + the current number we are on
                    # Is similar to right + down in recursive solution
                dp[col] += dp[col - 1] 
        
        # We are accumulating the states so return last number
        return dp[-1]
