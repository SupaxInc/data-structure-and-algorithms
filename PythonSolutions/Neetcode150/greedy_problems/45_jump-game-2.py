class BruteForceTopDownSolution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            # Base case 1: We reached end of the array
            if i >= n - 1:
                return 0
            # Base case 2: If we can't jump at all then return a really high number
            if nums[i] == 0:
                return float("inf")

            min_jumps = float("inf")

            for j in range(1, nums[i] + 1):
                if i + j < n:
                    jumps = dfs(i + j)
                    
                    # Update the minimum jumps if the new path requires fewer jumps
                    if jumps != float('inf'):
                        jumps += 1
                        min_jumps = min(min_jumps, jumps)
            
            cache[i] = min_jumps
            return min_jumps
        
        return dfs(0)

class GreedySolution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        farthestReach = 0
        currentEnd = 0
        jumps = 0

        for i in range(n):
            # Greedy choice: Select the farthest jump per iteration
            farthestReach = max(farthestReach, i + nums[i])

            # If we reach the farthest jump out of all previous iterations
            if i == currentEnd:
                # We need to jump again
                jumps += 1
                # Update our next end to the current farthest reach
                currentEnd = farthestReach
                
                # If our next end reachest farther than the length of the array or the end then stop
                if currentEnd >= n - 1:
                    break

        return jumps
                