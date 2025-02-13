class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combinations = []

        def backtrack(start, remainingToTarget):
            # Prune path if total becomes greater than target
            if remainingToTarget < 0:
                return
            
            if remainingToTarget == 0:
                res.append(combinations[:])
            
            for i in range(start, len(candidates)):
                # Include the current choice
                combinations.append(candidates[i])

                # Recurse, explore the current option deeper
                    # Continue with the same option UNTIL the path gets pruned or loop ends, allows us to reuse the same number
                backtrack(i, remainingToTarget - candidates[i])

                # Exclude the choice, backtrack to remove last added candidate and try other combinations
                combinations.pop()
            
        backtrack(0, target)
        return res
