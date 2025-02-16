class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combinations = []
        # Sort so that duplicates numbers are adjacent to each other
        candidates.sort()

        def backtrack(start, remainingToTarget):
            # Base case 1: Current sum was greater than the target, prune search
            if remainingToTarget < 0:
                return
            
            # Base case 2: Current sum hit the target, prune search since there will be no more combinations
            if remainingToTarget == 0:
                res.append(combinations[:])
                return
            
            for i in range(start, len(candidates)):
                # Check if there are adjacent duplicate numbers
                    # We are checking for start since options change when we explore a choice deeper
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # Inclusion choice: Add the current number
                combinations.append(candidates[i])

                # Explore the current choice (current combinations) deeper with new options
                    # We are adding i + 1 here so we don't use the same number more than once
                backtrack(i+1, remainingToTarget - candidates[i])

                # Exclusion choice: Remove the curent number then try new options in new loop iteration
                combinations.pop()
        
        backtrack(0, target)
        return res