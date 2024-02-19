class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Reverse through an array to 'carry a one' similar to long addition
        for i in range(len(digits)-1, -1, -1):
            # Just return if its not a 9, this works also if we do carry a 1
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # Change digit to 0 since were carrying a one to previous digit
            digits[i] = 0
        
        # Use list concatenation to 'unshift' and add a new value to beginning of list in Python
        return [1] + digits