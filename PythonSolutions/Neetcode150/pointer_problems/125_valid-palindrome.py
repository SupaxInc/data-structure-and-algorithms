import re

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
    
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        newString = ''

        # Create a non-alphanumeric string of the original string
        for char in s:
            if char.isdigit() or char.isalpha():
                newString += char.lower()

        # Compare if the non-alphanumeric string equals to the reverse of it
        return newString == newString[::-1]
            