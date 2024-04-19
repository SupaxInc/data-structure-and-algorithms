class BruteForceSolution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        
        def dfs(index, total):
            # Stop when we reach the end of nums array
            if index == len(nums):
                # Count a valid combination when total equals target
                return 1 if total == target else 0
            
            # Choice 1: Add the current number
            add = dfs(index + 1, total + nums[index])
            # Choice 2: Subtract the current number
            subtract = dfs(index + 1, total - nums[index])

            return add + subtract
        
        return dfs(0, 0)