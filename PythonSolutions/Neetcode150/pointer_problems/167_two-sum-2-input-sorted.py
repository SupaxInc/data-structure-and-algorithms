from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            total = numbers[l] + numbers[r]
            
            if total == target:
                return [l + 1, r + 1]

            # Move right pointer to left if total is greater
            # Move left pointer to right if total is smaller
            if total < target:
                l += 1
            else:
                r -= 1
            
        return []
