"""
- length of string can be from 1 to 100
- strings only contains digits
- string can have leading 0's (e.g. "06" is not valid but "6" is)
- answer can only fit in 32 bit interger

State: dp[i]
- i is the (i+1) index of the codes, since the current digit would be s[i-1] due to base cases
- dp[i] represents number of ways to decode the digits at that current substring

Base cases:
1. dp[0] = 1 (1 way to decode an empty string, "do nothing", not intuitive but typical dp problems need a "do nothing" case)
2. dp[1] = 1 (if s[i-1] (current digit at dp[1]) != "0", then 1, else 0)

Transition:
- For single digits, if s[i-1] (current digit) is not "0" then:
    dp[i] += dp[i-1] (all ways to decode up to previous position)

- For double digits, if s[i-2:i] (previous digit) is between 10 and 26:
    dp[i] += dp[i-2] (all ways to decode up to two positions back)

- We don't do something like dp[i-1] + 1 or dp[i-2] + 1 b/c we're not counting a new individual way
  we're counting all possible extensions of previous ways. If there were 3 ways to decode up to position i-1, 
  then there are 3 ways to extend those decodings with the current valid digit, not 3+1.

Returns: dp[n], length of string
"""
class NonOptimizedBottomUpSolution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # Early base case to prevent a "0" being counted as 1 way to decode during base cases
            # Leading zeros are not allowed as it invalidates the entire string,
            # e.g. "0243" -> 0 ways to decode 0 thus invalidating entire base cases
        if s[0] == "0":
            return 0

        # Initializing 1D dp array
            # ways[i] represents the number of ways to decode the substring at current point
        ways = [0] * (n + 1) # * n + 1 to account for the dp[0] base case *
        
        # Base cases:
        # * Not intuitive, but in dp, we often need a value for the "do nothing" case recurrence relation work correctly *
        ways[0] = 1 # (1 way to decode an empty string, "do nothing")
        ways[1] = 1 # (1 way to decode the first digit, if its not a "0" which is handled in early base case above)

        # Recurrence relation: At each index i, we can form a valid decoding in two ways:
        for i in range(2, n + 1):
            # Transition 1: For single digit, check if current digit (s[i-1]) is not a leading zero,
            if s[i-1] != "0":
                ways[i] += ways[i-1]
            
            # Transition 2: For double digits, check if previous digits is between 10 and 26,
            if 10 <= int(s[i-2:i]) <= 26:
                ways[i] += ways[i-2]
        
        return ways[-1]

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # Early base case to prevent a "0" being counted as 1 way to decode during base cases
            # Leading zeros are not allowed as it invalidates the entire string,
            # e.g. "0243" -> 0 ways to decode 0 thus invalidating entire base cases
        if s[0] == "0":
            return 0
        
        # Base cases:
        prev2 = 1 # 1 digit back (1 way to decode an empty string, "do nothing")
        prev1 = 1 # current digit (1 way to decode the first digit, if its not a "0" which is handled in early base above)

        # Recurrence relation: At each prev1 and prev2, we can form a valid decoding in two ways:
        for i in range(2, n + 1):
            current = 0 # Sum of both ways at current digit

            # Transition 1: For single digit, check if current digit (s[i-1]) is not a leading zero,
            if s[i-1] != "0":
                current += prev1
            
            # Transition 2: For double digits, check if previous digits is between 10 and 26,
            if 10 <= int(s[i-2:i]) <= 26:
                current += prev2

            # Move the references up 1
                # prev2 becomes prev1 (1 digit back becomes current digit)
                # prev1 becomes current (current digit back becomes new digit)
            prev2, prev1 = prev1, current
        
        # Return the current digit which contains all previous accumulations at that point in the substring
        return prev1
    
class TopDownSolution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def decode(index):
            # Base case 1: If index is already cached return the number of ways
            if index in memo:
                return memo[index]

            # Base case 2: If index hits empty string, return a 1 as theres 1 way to decode by "doing nothing"
            if index < 0:
                return 1
            
            # Initialize the number of ways for the current position index
            current = 0

            # Transition 1: For single digit, check if current digit is not "0"
            if s[index] != "0":
                current += decode(index-1)
            
            # Transition 2: For double digits, check if double digits is between 10 and 26
                # index > 0, helps prevent out of boundary on string
            if index > 0 and (10 <= int(s[index-1:index+1]) <= 26):
                current += decode(index-2)
            
            # Add answer to cache
            memo[index] = current
            return memo[index]
        
        # Begin the decode on the last digit to go from top down (reverse)
        return decode(len(s)-1)
