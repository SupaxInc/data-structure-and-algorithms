class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        minNum = float("inf")

        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            minNum = min(minNum, nums[mid])

            # It is rotated in a way that smaller numbers are on the left of the bigger number in mid
            if nums[mid] > nums[hi]: 
                # So move lo pointer to the right to find smaller numbers
                lo = mid + 1
            # If mid smaller than end, then its rotated in a way that smaller numbers are on the left
            else:
                # So move hi pointer to the left to find smaller numbers
                hi = mid - 1
        
        return minNum
        