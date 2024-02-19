class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Begin at 0 to cancel out num 0
        res = 0
        # Iterate through the array plus the max of array length
        # Helps cover all 0 to n numbers
        for i in range(0, len(nums) + 1):
            # Cancel out all nums in current array and prevent from accessing array out of bounds
            if i < len(nums): 
                res ^= nums[i]
            # Cancel out all nums in index, 0 to n
            res ^= i
        
        return res