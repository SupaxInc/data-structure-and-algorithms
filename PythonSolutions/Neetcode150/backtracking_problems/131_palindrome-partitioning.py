class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        pals = []

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            
            return True


        def backtrack(start):
            # Base case: Add to the result if our start boundary is greater than the length of input set
                # A palindrome partition requires all letters to be a part of the result
                # INCLUDING the last option which is why its not == but a >
            if start > len(s) - 1:
                res.append(pals[:])
                #  Prune since there would be no other options to find if we have checked all options now
                return

            for end in range(start, len(s)):
                # Check if current option substring is a palindrome
                if isPalindrome(start, end):
                    # Include current substring choice as a palindrome
                    pals.append(s[start:end+1])

                    # Explore more substring choices with the next letter
                    backtrack(end + 1)

                    # Exclude the current substring choice then move onto a new choice in next iteration
                    pals.pop()
        
        backtrack(0)
        return res
