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
        if not s:
            return ""

        def isPalindrome(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            # l and r at this point would be off by l - 1 and r + 1
                # So we need to return l+1, r is fine as its non-exclusive
            return s[l+1:r]
        
        longestPal = ""
        for i in range(len(s)):
            even = isPalindrome(i, i + 1) # Even length
            odd = isPalindrome(i, i) # Odd length

            if len(even) > len(odd):
                if len(even) > len(longestPal):
                    longestPal = even
            else:
                if len(odd) > len(longestPal):
                    longestPal = odd
            
        return longestPal
        
            
            