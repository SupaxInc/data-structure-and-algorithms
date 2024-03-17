class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start):
            # When start hits same index as length of nums
                # This means a complete permutation has formed
            if start == len(nums):
                result.append(nums[:])
                return

            for i in range(start, len(nums)):
                # Swap index and start
                nums[start], nums[i] = nums[i], nums[start]
                
                # Explore current index choice as deep as possible 
                backtrack(start + 1)

                # Undo swap
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return result