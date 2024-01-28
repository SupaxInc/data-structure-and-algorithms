from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}

        for i in range(len(nums)):
            numNeeded = target - nums[i]
            if numNeeded in myMap:
                return [myMap[numNeeded], i]
            myMap[nums[i]] = i
        
        return []