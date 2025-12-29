import re
class MostOptimalSolution:
    def isPalindrome(self, s: str) -> bool:
        # Two pointers: start and end
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters from left
            while left < right and not s[left].isalnum():
                left += 1
            
            # Skip non-alphanumeric characters from right
            while left < right and not s[right].isalnum():
                right -= 1
        
            # Compare non-alphanumeric characters (case-insensitive) after possibly skipping the characters
            if s[left].lower() != s[right].lower():
                return False
            
            # Move the pointers inward to check for the next pair of characters in next iteration
            left += 1
            right -= 1
        
        return True

class Solution1:
    def isPalindrome(self, s: str) -> bool:
        # Remove non-alphanumeric characters
        newString = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        # Create two pointers for the NEW string
        start = 0
        end = len(newString) - 1

        # Traverse through the new non-alphanumerical string
        for i in range(len(newString)):
            # It is not a palindrome if the start and end characters don't match
            if newString[start] != newString[end]:
                return False
            
            start += 1
            end -= 1
        
        return True
    
class SomewhatOptimalSolution:
    def isPalindrome(self, s: str) -> bool:
        # Convert characters into lowercases without alphanumerics
        # [EXPRESSION for ITEM in ITERABLE if CONDITION]
        chars = [char.lower() for char in s if char.isalnum()]
        # Check if it equals the reverse of it
        return chars == chars[::-1]