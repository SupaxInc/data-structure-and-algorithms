class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        start = 0
        mySet = set()

        for end in range(0, len(s)):
            # Shrink the window if the current index char is in the set (which means there is a duplicate)
            while s[end] in mySet and start <= end:
                # To shrink it we remove the start pointer char then continuously move it up
                
                # Continuously remove the start pointer char until the duplicate is removed
                mySet.remove(s[start])
                start += 1
            
            # Add the current index char if its no longer in the set
            mySet.add(s[end])
            maxLength = max(maxLength, (end-start) + 1)

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