class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        # Sort the numbers so that duplicate numbers are adjacent to each other
        nums.sort()

        def backtrack(start):
            # No need for a base case here
                # Our base case is the range of the for loop, function stack will pop when range finishes
            res.append(subset[:])

            for i in range(start, len(nums)):
                # Skip if the previous number is a duplicate number
                    # Effectively pruning the search for current branch
                    # We check if current index is greater than start since deeper depths means a new option
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                # Inclusion choice: Add the number
                subset.append(nums[i])

                # Explore current option (current subset) deeper with more numbers
                backtrack(i + 1)

                # Exclusion choice: Remove the number from current subset then try a new option in new loop iteration
                subset.pop()
        
        backtrack(0)
        return res