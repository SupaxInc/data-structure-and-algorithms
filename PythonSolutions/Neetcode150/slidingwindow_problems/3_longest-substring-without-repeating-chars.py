class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        start = 0
        mySet = set()

        for i in range(0, len(s)):
            # Shrink the window if the current index char is in the set
            while s[i] in mySet and start <= i:
                # To shrink it we remove the start pointer char then continuously move it up
                mySet.remove(s[start])
                start += 1
            
            # Add the current index char if its no longer in the set
            mySet.add(s[i])
            maxLength = max(maxLength, (i-start) + 1)

        return maxLength