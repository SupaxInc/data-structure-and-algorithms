class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res
        
        phoneNumber = { "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs",
                        "8": "tuv", "9": "wxyz" }

        def backtrack(digitIndex, pathCombination):
            # Prune search space if we find a valid combination, which backtracks to last recurse in callstack
            if len(digits) == len(pathCombination):
                res.append(pathCombination)
                return
            
            # Grab the letters for the digit index, this will be our choices
            letters = phoneNumber[digits[digitIndex]]
            # Iterate through all choices
            for letter in letters:
                # Inclusion choice: Add current choice letter to path
                backtrack(digitIndex + 1, pathCombination + letter)
                # Exclusion choice: Happens when call stack pops, it removes previous letter
                    # This is since the letter is being added in the params
                    # When call stack pops the params are changed

        backtrack(0, "")
        return res