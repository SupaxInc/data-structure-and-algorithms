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

#* This is now failing with memory limit exceeded *
class OptimizedTopDownSolution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        
        # Early return: Sum is odd which means two subsets would never be equal
        if (totalSum % 2) != 0:
            return False

        # The target we need for a subset is half of total sum
        target = totalSum // 2
        memo = {}
        
        # States: Returns true or false if two subsets equal each other
            # State 1: currIdx, position at current array
            # State 2: remainingSum, sum that is remaining to hit half of total sum (makes subsets equal)
                # *Remaining sum is used over Curr sum since it helps catch early stopping conditions a lot earlier
                # * comapred to brute force solution *
                # Prevents unncessary states in memory
        def canFindEqualPartition(currIdx, remainingSum):
            # Base case 1: Current subset is already in the cache
            if (currIdx, remainingSum) in memo:
                return memo[(currIdx, remainingSum)]

            # Base case 2: Subset was found that equals half the total sum (target)
            if remainingSum == 0:
                return True
            
            # Base case 3: Boundary cases
                # - We passed the length of numbers array
                # - OR we went past the remaining sum (negatives)
            if currIdx >= len(nums) or remainingSum < 0:
                return False
            
            # Include, Exclude, Backtracks
                # Backtracking will be done through the function parameter
            include = canFindEqualPartition(currIdx + 1, remainingSum - nums[currIdx])
            exclude = canFindEqualPartition(currIdx + 1, remainingSum)

            memo[(currIdx, remainingSum)] = include or exclude

            return memo[(currIdx, remainingSum)]
        
        return canFindEqualPartition(0, target)

class OptimizedBottomUpSolution:
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