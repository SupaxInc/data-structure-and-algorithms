class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(start):
            # No need for a base case, for loop takes care of only constraint
                # Which is to stop recursing when we reach the length of nums

            # Append subset right away to include empty subsets
                # Also adds a new subset to result per recursion
            result.append(subset[:]) # Deep copy

            # Iterate through all choices we have
            for i in range(start, len(nums)):
                # Append the choice (inclusion)
                subset.append(nums[i])
                
                # Explore the choice deeper
                backtrack(i + 1)

                # Undo the choice (exclusion)
                subset.pop()

        # Begin at the first choice
        backtrack(0)
        return result