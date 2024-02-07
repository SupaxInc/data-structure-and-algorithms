from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1

        while lo <= hi:
            mid = lo + ((hi - lo) // 2) # A normal (hi + lo) // 2 could lead to an arithmetic overflow

            if nums[mid] == target:
                return mid

            # Move to the right side of the array, add a 1 to exclude the current mid index we are on
            if nums[mid] < target:
                lo = mid + 1
            # Move to the left side of the array, substract a 1 to exclude the current mid index we are on
            elif nums[mid] > target:
                hi = mid - 1
        
        return -1