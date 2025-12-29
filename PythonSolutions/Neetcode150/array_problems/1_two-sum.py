from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myNums = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in myNums:
                return [myNums[complement], i]
            
            myNums[num] = i
        
        return []