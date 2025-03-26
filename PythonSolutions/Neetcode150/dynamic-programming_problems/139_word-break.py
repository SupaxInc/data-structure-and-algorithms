"""
- the entire string s must be broken until the end of string, if not its a fail. 
    - e.g. dogqwasdqwe, can only break dog
- we need to try all possibilities in the word dictionary to get a solution where the entire word can be broken
- the same word can be used multiple times
- Brute force naive: a naive nested for loop would fail since it would be hard to find the end of words per each combination
    - e.g. s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    - we need to try if all words here can break the word, try breaking word from cats if that doesn't work then cat, etc

State: dp[i] represents if PREVIOUS string index has been segmented with a word

Recurrence Relation: At each index i, check if the word is in the dictionary and can be segmented
Transition: dp[end] = True
    - makes the end of string a True so that in next iteration we can check if new start (previous end) had a word

Base cases:
1. dp[0] = True, an empty string can be segmented
    - Helps us transition the beginning word since we require a check to see if previous end was a word
    - NOTE: This shifts the dp indices over by 1 to the LEFT compared to the string index

Returns: dp[len(s)], if end of string is a word then we successfully were able to break all the words
"""
class OptimizedSolution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Initialize dp array
            # State: dp[i], if the string up to index i-1 can be segmented
            # e.g. s = leetcode, dp[0] = empty string (before word leetcode) while s[0] = "l"
        n = len(s) + 1 # + 1 to account for base case
        # NOTE: This shifts the dp indices over by 1 to the LEFT compared to the string index
        wordBreaks = [False] * n

        # Base case: The previous word before string s would be an empty string
        wordBreaks[0] = True

        # Turn word dictionary into a set for faster lookups
        wordDict = set(wordDict)

        # End helps create an upper boundary so we can string slice a word
        for end in range(1, n):
            # Partition the strings so we can find segments from start to end
                # e.g. pineapp, ineapp, neapp, eapp, "app" is a segment
            for start in range(end):
                word = s[start:end] # No need to do end+1 since we skipped due to base case

                # Transition: Check if the word is in dictionary AND if the string up to start can be segmented
                if word in wordDict and wordBreaks[start]:
                    # Mark end as True, meaning s[0:end] can be segmented (whole current string)
                    # NOTE: Remember that dp indices are shifted to the left 
                    wordBreaks[end] = True

                    # No longer need to check for a word in current start to end range
                    # Check next end + 1 if there is another word and we begin from start again, 
                    # to check if whole string again can be segmented
                    break 
        
        # Return dp[len(s)], which indicates if the entire string can be segmented
        return wordBreaks[len(s)]

class BruteForceBacktrackingSolution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Turn dictionary into a set for faster lookup
        wordDict = set(wordDict)

        # We begin at start, allows us to set an upper boundary for looping through string
        def wordCanBreak(start):
            # Base case 1: We are now at end of string, getting to the end means there is a word here (see explore below)
            if start == len(s):
                return True
            
            # Explore if each substring can break starting at the start index
                # start+1 since string slicing at the end is non-inclusive
                # len(s)+1 to account for the start+1
            for end in range(start+1, len(s)+1):
                # Create the word using string slicing
                word = s[start:end]

                # Base case 2: Word is found and it can break at the end of the word
                    # wordCanBreak will explore the new index option as deep as possible to check if there is a word
                    # and a word and a word and a word until the end which pops the stack and tells us there was a word break
                if word in wordDict and wordCanBreak(end):
                    return True

            # If a word could not be found after testing all substrings at start, then return False
            return False
        
        # Begin the search at the first character
        return wordCanBreak(0)
class TopDownSolution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        memo = {}
        
        def canBreak(start):
            # If we've already computed this subproblem, return the cached result
            if start in memo:
                return memo[start]
            
            # Base case: reached the end of string successfully
            if start == len(s):
                return True
                
            # Try all possible words starting from current position
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                
                # If the word is in dictionary and the rest of string can be broken
                if word in wordDict and canBreak(end):
                    # Adds the start as the key since it tells us we can break the future word from top down (backwards)
                    memo[start] = True
                    return True
            
            # If no valid word break found
            memo[start] = False # Adds the start as the key since it tells us we can break the future word from top down (backwards)
            return False
        
        return canBreak(0)
