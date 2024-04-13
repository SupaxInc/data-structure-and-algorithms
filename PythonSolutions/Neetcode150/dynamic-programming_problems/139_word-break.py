class BruteForceSolution:
    def wordBreak(s, wordDict):
        def canBreak(start):
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordDict and canBreak(end):
                    return True
            return False
        
        # Convert the list of words into a set for faster lookup
        wordDict = set(wordDict)
        return canBreak(0)

    # Example usage
    s = "pineapple"
    wordDict = ["pine", "app", "apple"]
    print(wordBreak(s, wordDict))  # Output: True

class OptimizedSolution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s) + 1
        wordDict = set(wordDict) 

        dp = [False] * n
        # Base case, 1 way to segment empty string
        dp[0] = True

        for end in range(1, n):
            # Partition the strings so we can find segments from start to end
                # E.g. pineapp, ineapp, neapp, eapp, "app" is a segment
            for start in range(end):
                word = s[start:end]
                # Check if the start of the partition dp[start] is cached 
                    # which means there was a word there that was segmented
                if dp[start] and word in wordDict:
                    dp[end] = True
                    break # Break since we no longer need to look for any more segments in partition

        return dp[len(s)] 
