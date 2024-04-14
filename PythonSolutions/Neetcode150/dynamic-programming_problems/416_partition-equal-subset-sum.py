class BruteForceSolution:
    def canPartition(nums):
        total_sum = sum(nums)
        # Early exit if the total sum is odd
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2

        def canFindSubset(current_index, current_sum):
            # Base case: found a subset with the desired sum
            if current_sum == target:
                return True
            # Out of bounds or sum exceeded the target
            if current_index >= len(nums) or current_sum > target:
                return False
            
            # Include the current number in the subset
            include = canFindSubset(current_index + 1, current_sum + nums[current_index])
            # Exclude the current number from the subset
            exclude = canFindSubset(current_index + 1, current_sum)

            return include or exclude

        return canFindSubset(0, 0)

# Example usage
nums = [1, 5, 11, 5]
print(canPartition(nums))  # Output: True

class MemoizedSolution:
    def canPartition(nums):
        total_sum = sum(nums)
        # Check if the total sum is even
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        memo = {}

        def canFindSubset(current_index, remaining_sum):
            # If we have reached the target sum
            if remaining_sum == 0:
                return True
            # Out of bounds or no remaining sum to consider
            if current_index >= len(nums) or remaining_sum < 0:
                return False
            # Check memoization
            if (current_index, remaining_sum) in memo:
                return memo[(current_index, remaining_sum)]
            
            # Include or exclude the current number
            include = canFindSubset(current_index + 1, remaining_sum - nums[current_index])
            exclude = canFindSubset(current_index + 1, remaining_sum)

            # Store the result in memoization table
            memo[(current_index, remaining_sum)] = include or exclude
            return memo[(current_index, remaining_sum)]

        return canFindSubset(0, target)

class OptimizedTopDownSolution:
    def canPartition(nums):
        total_sum = sum(nums)
        # If the total sum is odd, it's impossible to split the array into two equal subsets
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        # Initialize a DP array where dp[j] means whether a subset with sum j can be formed
        dp = [False] * (target + 1)
        dp[0] = True  # A sum of 0 is always possible because we can choose an empty subset

        # Iterate over each number in the input array
        for num in nums:
            # Traverse the dp array from right to left to prevent reusing the same element
            # in the same iteration. This approach ensures that each number is only used once per
            # subset sum calculation.
            for j in range(target, num - 1, -1):
                currSum = j - num
                # If a subset with sum j - num was previously possible,
                # then a subset with sum j is also possible by including this number.
                if dp[j - num]:
                    dp[j] = True

        # The value at dp[target] will be True if a subset with sum equal to target can be formed,
        # meaning the original array can be split into two subsets with equal sums.
        return dp[target]