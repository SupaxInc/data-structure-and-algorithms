class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = lo + ((hi - lo) // 2)

            if nums[mid] == target:
                # Return index
                return mid
            
            # In left sorted portion of array
            if nums[mid] > nums[hi]:
                # Search right if array is rotated where the target is on the right portion of array
                # Or if its still in left sorted portion but greater than our current mid number
                if target < nums[lo] or target > nums[mid]:
                    lo = mid + 1
                # Search left if target is within the left sorted portion
                else:
                    hi = mid - 1
            # In right sorted portion of array
            else:
                # Search left if array is rotated where the target is on left portion of array
                # Or if its still in right sorted portion but less than our current mid number
                if target > nums[hi] or target < nums[mid]:
                    hi = mid - 1
                # Search right if target is in right sorted portion
                else:
                    lo = mid + 1

        return -1 