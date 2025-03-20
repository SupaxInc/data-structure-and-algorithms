"""
Literally almost the same as leetcode 647, instead of finding longest palindrome it counts all palindromes
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def isPalindrome(l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1 
            
            return count

        for i in range(len(s)):
            count += isPalindrome(i, i + 1) # Even length
            count += isPalindrome(i, i) # Odd length

        return count