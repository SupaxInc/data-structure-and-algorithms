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
            # If a subset with sum j - num was previously possible,
            # then a subset with sum j is also possible by including this number.
            if dp[j - num]:
                dp[j] = True

    # The value at dp[target] will be True if a subset with sum equal to target can be formed,
    # meaning the original array can be split into two subsets with equal sums.
    return dp[target]

# Example usage
nums = [1, 5, 11, 5]
print(canPartition(nums))  # Output: True
