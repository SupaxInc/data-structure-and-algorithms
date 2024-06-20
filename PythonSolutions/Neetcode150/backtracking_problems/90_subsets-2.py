class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort() # Sort so duplicates are adjacent to each other

        def backtrack(start):
            res.append(subset[:])
            
            # Iterate through the choices
            for i in range(start, len(nums)):
                # Prune the search if we find a duplicate adjacent to each other
                    # Example of a duplicate: [1, 2, 2]
                    # [1, 2] and [1, 2] could happen
                if i > start and nums[i] == nums[i-1]:
                    continue

                # Include the choice
                subset.append(nums[i])

                # Explore the choice as deep as possible
                backtrack(i+1)

                # Remove the choice
                subset.pop()

        backtrack(0)
        return res
