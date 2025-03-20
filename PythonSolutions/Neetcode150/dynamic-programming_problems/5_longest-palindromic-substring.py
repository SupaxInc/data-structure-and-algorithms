class BruteForceSolution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(substring):
            return substring == substring[::-1] # O(n)
        
        longestPal = ""

        for i in range(len(s)): # O(n)
            for j in range(i, len(s)): # O(n)
                substr = s[i:j+1]
                if len(substr) > len(longestPal) and isPalindrome(substr):
                    longestPal = substr
        
        return longestPal

class OptimizedSolution:
    def longestPalindrome(self, s: str) -> str:
        longestPal = ""
        
        for i in range(len(s)):
            # Expand the center to find even or odd palindromes
                # E.g. "baab" is even, and "bab" is odd
            odd = self.isPalindrome(i, i, s)
            even = self.isPalindrome(i, i+1, s)

            # Check if the odd or even are the longest palindromes
            if len(even) > len(odd):
                # Check if its longer than current longest palindrome
                if len(even) > len(longestPal):
                    longestPal = even
            else:
                if len(odd) > len(longestPal):
                    longestPal = odd
        
        return longestPal

    # Expand around center palindrome check
    def isPalindrome(self, l, r, s):
        # While condition:
            # - left and right is within the string 
            # - left character is equal to the right character
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # Move left backwards to expand
            l -= 1
            # Move right backwards to expand
            r += 1
        
        # Left will be 1 index off due to expanding once more to break while condition
        # Right is 1 index off but end of string separator is non inclusive
        return s[l+1:r]
        
            
            