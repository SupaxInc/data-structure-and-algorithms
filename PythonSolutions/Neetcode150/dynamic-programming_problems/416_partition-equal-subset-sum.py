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
