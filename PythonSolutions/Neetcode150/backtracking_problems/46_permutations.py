class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start):
            # When start hits same index as length of nums
                # This means a complete permutation has formed
            if start == len(nums):
                result.append(nums[:]) # Deep copy
                return

            for i in range(start, len(nums)):
                # Swap index and start
                nums[start], nums[i] = nums[i], nums[start]
                
                # Explore current index choice as deep as possible 
                    # Changes the range of the for loop from start + 1 to len(nums)
                    # E.g. [1, 2, 3]
                    # Initial -> Idx: 0 to 3 [1, 2, 3] -> Explore -> 1 to 3 [2, 3] -> 
                    # Explore -> 2 to 3 [3] -> Explore -> 3 to 3 [] -> Hits Base Case
                # We are using start here instead of index i because think of it like:
                    # start = "Which positions do I want to look for all permutations for next?"
                    # i = "Which number do I want to test for permutations?"
                    # Start makes more sense since we want to try permutations for all the next numbers over rather than just selecting a specific number
                backtrack(start + 1)

                # Undo swap
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return result