class BruteForceSolution:
    def canJump(self, nums: List[int]) -> bool:
        def dfs(i):
            # Base case: Jumped enough to reach end of list
            if i == len(nums) - 1:
                return True
            
            # Begin at 1 to prevent unnecessary jump from 0
                # The constraint is that the nums in list are never 0 or negative
            for j in range(1, nums[i] + 1):
                res = dfs(i + j)
                # If at any point we reached end of list, then just end loop
                if res:
                    return True

            # Return false if no valid path was found
            return False
        
        return dfs(0)

class TopDownSolution:
    def canJump(self, nums: List[int]) -> bool:
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            # Base case: Jumped enough to reach end of list
            if i == len(nums) - 1:
                return True
            
            # Boundary check to prevent jumping out of the list index
                # Find min for: 
                    # Our current position + max current jump length
                    # Or the length of array  
                # Prevents unnecessary recursion 
            furthestJump = min(i + nums[i], len(nums) - 1)

            # Begin at furthest possible jump
                # Prevents more unnecessary recursion
            for j in range(furthestJump, i, -1):
                if dfs(j):
                    cache[i] = True
                    return cache[i]

            # Return false if no valid path was found
            cache[i] = False
            return False
        
        # Begin at index 0
        return dfs(0)

class BottomUpSolution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n

        dp[0] = True # First index is always reachable

        for i in range(n):
            if dp[i]: # If current index is reachable then try all jump lengths
                for j in range(1, nums[i] + 1):
                    # Cache the jump length if we were able to jump without reaching the boundary
                    if i + j < n:
                        dp[i + j] = True
                    # If we already ended up at the end, just early return
                    if i + j == n - 1:
                        return True
        
        # The last index in the DP indicates if the last index was reachable
        return dp[n - 1]