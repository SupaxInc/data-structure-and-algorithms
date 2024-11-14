class MySolution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowLength = len(s1)
        if windowLength < 1:
            return False

        s1Count = defaultdict(int)
        s2Count = defaultdict(int)
        start = 0
    
        for char in s1: # O(n)
            s1Count [char] += 1

        for end in range(0, len(s2)): # O(m)
            s2Count[s2[end]] += 1

            # Check for criterias when its finally at its fixed window length
            if end >= windowLength - 1:
                # If the char occurences are the same for both count maps then there are permutations
                if s1Count == s2Count: # O(26)
                    return True

                # Move the fixed size window by decrementing the count
                s2Count[s2[start]] -= 1
                # If the count is zero, remove it from the map.
                # Allows us to properly compare between the string 1 and string 2 count
                if s2Count[s2[start]] == 0:
                    s2Count.pop(s2[start])
            
                # Increment the start pointer so it stays within fixed window length
                start += 1

        return False
    
class MostOptimalSolution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = defaultdict(int)
        for char in s1:
            s1Count[char] += 1

        matches = 0
        start = 0
        for end in range(len(s2)):
            # Add the new character to the window
            if s2[end] in s1Count:
                s1Count[s2[end]] -= 1
                # If the frequency of the character is 0, then we increment the matches as its a match for the permutation
                if s1Count[s2[end]] == 0:
                    matches += 1
            
            # Remove the character leaving the window if we are at fixed window size
            if (end-start) + 1 > len(s1):
                if s2[start] in s1Count:
                    # If the frequency of the start character is 0, then we decrement the matches as its no longer a match
                    if s1Count[s2[start]] == 0:
                        matches -= 1
                    s1Count[s2[start]] += 1
                
                # Increment the start pointer so it stays within fixed window length
                start += 1
                
            # If all characters match, return True
            if matches == len(s1Count):
                return True
        
        return False