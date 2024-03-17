class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        combinations = []

        # Remaining to target allows us to keep track of total so we can equal to target
        def backtrack(start, remainingToTarget):
            # Prune search if our total is greater than the target
            if remainingToTarget < 0:
                return
            
            # Add to result if our total is equal to target
            if remainingToTarget == 0:
                result.append(combinations[:])
            
            # Iterate through all choices
            for i in range(start, len(candidates)):
                # Include the current choice (inclusion)
                combinations.append(candidates[i])

                # Explore current choice as deep as possible, stay on current index
                    # Current index allows us to explore duplicates until total is greater than target
                backtrack(i, remainingToTarget - candidates[i])

                # Exclude the choice (exclusion)
                    # We can then iterate to next choice
                    # At this point we can also have duplicates in our combinations
                combinations.pop()

        backtrack(0, target)
        return result