class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(start):
            # No need for a base case, for loop takes care of only constraint
                # Which is to stop recursing when we reach the length of nums
            res.append(subset[:])

            for i in range(start, len(nums)):
                # Include the choice
                subset.append(nums[i])

                # Recurse, explore the next option deeper
                backtrack(i+1)

                # Exclude, backtrack to previous choice
                subset.pop()
        
        backtrack(0)
        return res
