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