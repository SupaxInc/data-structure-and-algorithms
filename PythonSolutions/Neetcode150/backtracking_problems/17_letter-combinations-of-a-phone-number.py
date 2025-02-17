class MoreEfficientSolution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits: 
            return res
        
        # Create a digit map for the telephone buttons
        digitMap = { "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz" }
        path = []

        def backtrack(digitIdx):
            # Base case: Path is the same length as digits
            if len(path) == len(digits):
                # Turn path into a string
                res.append("".join(path)) 
                # Prune the path since there are no more combinations to look for
                return
            
            # Grab the letters for the digit of the phone number
            letters = digitMap[digits[digitIdx]]

            for letter in letters:
                # Inclusion choice: Add the letter
                path.append(letter)

                # Explore the current path (current letters) as deep as possible until we hit the digits length
                backtrack(digitIdx + 1)

                # Exclusion choice: Remove the letter and try other options
                path.pop()

        backtrack(0)
        return res


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        if not digits:
            return res

        digitsMap = { "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz" }

        def backtrack(digitIdx, path):
            # Base case: We reached the end of the options for the current digit
            if digitIdx == len(digits):
                res.append(path)
                # Prune we can't choose any more choices as we've hit the length of digits
                return
            
            # Get the letters for current digit options
            letters = digitsMap[digits[digitIdx]]

            for letter in letters:
                # Inclusion choice: Choose the current letter
                    # We track the choices in the param
                # Explore the current choice (current path) deeper using the next digit
                backtrack(digitIdx + 1, path + letter)
                # Exclusion choice: When we backtrack out of the function it removes the added letter in the params
        
        backtrack(0, "")
        return res
        
