def wordBreak(s, wordDict):
    wordDict = set(wordDict)  # Use a set for O(1) average lookup time
    dp = [False] * (len(s) + 1)
    dp[0] = True  # Base case: empty substring is always true

    for i in range(1, len(s) + 1):
        for j in range(i):
            word = s[j:i]
            if dp[j] and word in wordDict:
                dp[i] = True
                break  # No need to continue if one valid segment is found

    return dp[len(s)]

# Example usage
s = "pineapple"
wordDict = ["pine", "app", "apple"]
print(wordBreak(s, wordDict))  # Output: True
