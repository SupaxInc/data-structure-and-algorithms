class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        maxLength = 0
        start = 0
        # Begin at the start pointer and add to set right away
        charSet = set(s[start])

        # Skip an index so our end pointer is on the 1st index
        for end in range(1, len(s)):
            # If the dynamic window shrunk too much or if end ptr is in the set
            while start <= end and s[end] in charSet:
                # Remove from char set and increment start pointer
                charSet.remove(s[start])
                start += 1

            # After no more duplicates in window add to set and calculate max length
            charSet.add(s[end])
            maxLength = max(maxLength, len(charSet))
        
        return maxLength 
    
# *O(n^3) time complexity*
class BruteForceSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        
        # Generate all possible substrings
        for i in range(len(s)): # O(n^2)
            for j in range(i, len(s)):
                # Get current substring
                current = s[i:j+1]

                # Convert to set to check for duplicates
                # If length of set equals length of substring, no duplicates exist
                # O(n) to convert to set
                if len(set(current)) == len(current):
                    maxLength = max(maxLength, len(current))
        
        return maxLength