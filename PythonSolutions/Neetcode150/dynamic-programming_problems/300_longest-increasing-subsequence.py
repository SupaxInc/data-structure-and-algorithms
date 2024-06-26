class BruteForceDFSSolution:
    def lengthOfLIS(nums):
        def is_increasing(subsequence):
            for i in range(len(subsequence) - 1):
                if subsequence[i] >= subsequence[i + 1]:
                    return False
            return True

        def generate_subsequences(index, current_subsequence):
            if index == len(nums):
                # When the end of the array is reached, check if the current subsequence is increasing
                if is_increasing(current_subsequence):
                    return len(current_subsequence)
                return 0
            
            # We have two choices per index, to include or not include the number to the current subsequence, makes O(2^n)
                # Include nums[index] in the subsequence
            taken = generate_subsequences(index + 1, current_subsequence + [nums[index]])
                # Do not include nums[index] in the subsequence
            not_taken = generate_subsequences(index + 1, current_subsequence)
            
            return max(taken, not_taken)

        # Start the recursive generation from the first element
        return generate_subsequences(0, [])

# Example usage
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(lengthOfLIS(nums))  # Output will depend on the input array's contents


class OptimizedSolution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Value of 1 since each number is a longest subsequence in of itself
        dp = [1] * (len(nums))

        for end in range(len(nums)):
            # Partition the subsequences
            for start in range(end):
                # Check if any number in the partition is smaller than the current number we are on
                if nums[start] < nums[end]:
                    # Cache the state, choose between max of current state or previous state + 1
                        # Current state may change per iteration 
                        # Previous states could have had its own subsequences where numbers were smaller than it
                    dp[end] = max(dp[end], dp[start] + 1)
        
        # Return the max subsequence count 
        return max(dp)