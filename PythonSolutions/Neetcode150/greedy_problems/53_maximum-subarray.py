class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        result = float("-inf")
        currSum = 0

        for num in nums:
            currSum += num
            # Check for max sum right away in the case that we have an array of all negatives
            result = max(result, currSum) 

            # Greedy choice: If current sum ever goes negative, then restart the subarray
            if currSum < 0:
                currSum = 0
            
        return result
