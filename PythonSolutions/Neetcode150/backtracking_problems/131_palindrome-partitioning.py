class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        pals = []

        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left, right = left + 1, right - 1
            return True

        def backtrack(start):
            # Prune the search space when we finish finding all of the palindromes for current substring
            if start > len(s)-1:
                res.append(pals[:])
                return
            
            for end in range(start, len(s)):
                # The choices are the palindrome substrings
                if isPalindrome(start, end):
                    # Include the palindrome (inclusion choice)
                    pals.append(s[start:end+1])

                    # Explore the palindrome further and partition it
                    backtrack(end+1)

                    # Exclude the palindrome (exclusion choice)
                    pals.pop()

        backtrack(0)
        return res