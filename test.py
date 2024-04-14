def lengthOfLIS(nums):
    if not nums:
        return 0

    # Step 1: Initialize the DP array
    dp = [1] * len(nums)

    # Step 2: Fill the DP table
    for i in range(len(nums)):
        for j in range(i):
            numJ = nums[j]
            numsI = nums[i]
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    # Step 3: The result is the maximum value in the DP table
    return max(dp)

# Example usage
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(lengthOfLIS(nums))  # Output should be 4
