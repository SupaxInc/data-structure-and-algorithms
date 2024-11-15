class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sCount = defaultdict(int)
        tCount = defaultdict(int)

        for char in t:
            tCount[char] += 1
        
        start = 0
        have, need = 0, len(tCount) # The amount of letters we have compared to what we need
        res, resLen = [0, 0], float("infinity") # Keep track of start and end of the result as well as the length
        for end in range(len(s)):
            sCount[s[end]] += 1
            # Check if current end char is part of string t and if the counts are the same 
            if s[end] in tCount and sCount[s[end]] == tCount[s[end]]:
                have += 1 # Increase the amount of letters required that we now have
            
            # The frequency of t is satisfied by current substring window
            while have == need:
                # Save the current result if the window is smaller then previous result length
                if (end - start + 1) < resLen:
                    res = [start, end]
                    resLen = end - start + 1
                
                # Try and make the window smaller to get a more minimum window
                sCount[s[start]] -= 1
                # Check if the current start char satisfies the frequency of string t
                if s[start] in tCount and sCount[s[start]] < tCount[s[start]]:
                    have -= 1 # Decrease the amount of letters that have been satisfied
                
                start += 1 # Shrink the window
        
        start, end = res
        return s[start : end + 1] if resLen != float("infinity") else ""
