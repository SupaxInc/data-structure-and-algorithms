class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sCount = defaultdict(int)
        tCount = defaultdict(int)

        for char in t:
            tCount[char] += 1
        
        start = 0
        have, need = 0, len(tCount) # The amount of letters we have compared to what we need
        res, resLen = [0, 0], float("infinity")
        for end in range(len(s)):
            sCount[s[end]] += 1
            # Check if current end char is part of string t and if the counts are the same 
            if s[end] in tCount and sCount[s[end]] == tCount[s[end]]:
                have += 1 # Increase the amount of letters required that we have now have
            
            # When we have the required amount of letters, we need to shrink the window to find more minimum
            while have == need:
                # Update the results if we found a more minimum length
                if (end - start + 1) < resLen:
                    res = [start, end]
                    resLen = end - start + 1
                
                # Remove the letter from the beginning of the window
                sCount[s[start]] -= 1
                if s[start] in tCount and sCount[s[start]] < tCount[s[start]]:
                    have -= 1 # Decrease amount of letters required
                
                start += 1 # Shrink the window
        
        start, end = res
        return s[start : end + 1] if resLen != float("infinity") else ""
