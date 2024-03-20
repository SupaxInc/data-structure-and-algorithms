def letterCombinations(digits: str) -> [str]:
    if not digits:
        return []
    
    # Mapping of digits to letters
    digit_to_char = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                     "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    
    results = []
    
    def backtrack(index: int, path: str):
        # If the path is the same length as digits, we've found a combination
        if len(path) == len(digits):
            results.append(path)
            return
        
        # Get the letters that the current digit maps to,
        # and loop through them
        possible_letters = digit_to_char[digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    # Start backtracking from the first digit
    backtrack(0, "")
    
    return results

letterCombinations("23")