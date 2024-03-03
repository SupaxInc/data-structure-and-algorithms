class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        minNum = float("inf")

        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            minNum = min(minNum, nums[mid])

            # If the number in the middle is greater than the number at the end
            # Then we search on the right side of the array
            # This is because the array will be sorted in a way that the min numbers are on the right
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return minNum