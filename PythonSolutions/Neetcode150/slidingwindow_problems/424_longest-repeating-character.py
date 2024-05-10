class MySolution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        maxLength = 0
        start = 0

        for i in range(0, len(s)):
            count[s[i]] += 1

            # Shrink the window if the total replacement is greater than k
            # Total replacement: size of window - max count within frequency map
            # This is because the max would be classified as the longest repeating character
                # AND the length subtract the max repeating character would equal the amount we have to replace
            while ((i - start) + 1) - max(count.values()) > k:
                count[s[start]] -= 1
                start += 1
            
            maxLength = max(maxLength, (i - start) + 1)
        
        return maxLength

class OptimizedSolution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        maxLength = 0
        maxFreq = 0  # Track the frequency of the most frequent character in the window
        start = 0

        for end in range(len(s)):
            count[s[end]] += 1
            
            # Update maxFreq if the current character's frequency is the highest seen so far
            maxFreq = max(maxFreq, count[s[end]])

            # Calculate the length of the current window minus the count of the most frequent character
            # If this difference is greater than k, shrink the window from the left
            while (end - start + 1) - maxFreq > k:
                count[s[start]] -= 1
                # Instead of recalculating maxFreq here, just shrink the window
                # maxFreq only decreases when the character with maxFreq is removed from the window
                # This is a key optimization that avoids recalculating max(count.values())
                start += 1
            
            # Update maxLength after possibly shrinking the window
            maxLength = max(maxLength, end - start + 1)
        
        return maxLength