from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] == target:
                return mid

            # Using mid as pivot, we can find out if we are in left or right sorted portion
            if nums[mid] > nums[hi]: # In left sorted portion
                # Search in right of array if:
                    # Target < Lo (target ends up in right sorted portion)
                    # Target > mid (target is still in left sorted portion)
                if target < nums[lo] or target > nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else: # In right sorted portion
                # Search in left of array if:
                    # Target > Hi (target ends up in left sorted portion)
                    # Target < Mid (target is still in right sorted portion)
                if target > nums[hi] or target < nums[mid]:
                    hi = mid - 1
                else: 
                    lo = mid + 1
            
        return -1