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
    
class TopDownSolution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        cache = {}
        
        def dfs(index, total):
            if (index, total) in cache:
                return cache[(index, total)]
            # Stop when we reach the end of nums array
            if index == len(nums):
                # Count a valid combination when total equals target
                return 1 if total == target else 0
            
            # Choice 1: Add the current number
            add = dfs(index + 1, total + nums[index])
            # Choice 2: Subtract the current number
            subtract = dfs(index + 1, total - nums[index])

            cache[(index, total)] = add + subtract
            return cache[(index, total)]
        
        return dfs(0, 0)

class BottomUpSolution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        # If target is out of the possible sum range
            # E.g [1, 1] -> -2 to 2, greater than 2 means we can't even reach to the sum
        if abs(target) > total_sum:
            return 0
        
        # Offset for zero index based access
        offset = total_sum
        
        # Create a DP array initialized to zero
        dp = [0] * (2 * total_sum + 1)
        
        # Initialize the base case
        dp[offset] = 1  # There's one way to make sum zero with no elements
        
        # Process each number in the array
        for num in nums:
            next_dp = [0] * (2 * total_sum + 1)
            for sum_idx in range(2 * total_sum + 1):
                if dp[sum_idx] != 0:
                    # If adding the number stays within bounds, add the ways to the new sum position after addition
                    if sum_idx + num <= 2 * total_sum:
                        next_dp[sum_idx + num] += dp[sum_idx]
                    # If subtracting the number stays within bounds, add the ways to the new sum position after subtraction
                    if sum_idx - num >= 0:
                        next_dp[sum_idx - num] += dp[sum_idx]
            dp = next_dp  # Move to the next state

        # Return the number of ways to achieve the target sum with all items considered
        return dp[offset + target]