class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        combinations = []

        def backtrack(start, remainingToTarget):
            # Constraint #1: Total cannot exceed target
            if remainingToTarget < 0:
                return
            
            # Constraint #2: Prune search space after finding valid combination
                # Helps avoid identical subsets
            if remainingToTarget == 0:
                res.append(combinations[:])
                return

            # Iterate through all choices
            for i in range(start, len(candidates)):
                # Constraint #3: Look for adjacent duplicats when we backtrack then go to next choice
                    # Prevents duplicates since if we backtrack, the prev index choice may be a duplicate
                    # Example: [1, 2, 2], target = 3
                    # [1, 2] and [1, 2] are the same solution sets
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # Inclusion choice
                combinations.append(candidates[i])
                # Explore choice as deep as possible
                backtrack(i + 1, remainingToTarget - candidates[i])
                # Exclude previous choice
                combinations.pop()

        backtrack(0, target)
        return res