class NonOptimizedBottomUpSolution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        length = len(s)

        # Initialize 1D Vector DP, length+1 to include base case
        dp = [0] * (length + 1)

        # Base cases:
            # dp[0] -> empty substring, symbolizing one way to decode it (doing nothing).
            # dp[1] -> one way to decode number from 1 to 9
        dp[0], dp[1] = 1, 1

        for i in range(2, length + 1):
            # Check for single digit (1-9) 
            # Add dp[i-1] because each previous decoding way can include this new valid single digit.
                # s[i-1] is current digit we are on, remember dp array is length + 1
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            # Check for double digit (10-26)
            # Add dp[i-2] since it represents the total number of ways the substring ending two characters 
            # before the current one can be decoded
                # s[i-2] is the previous digit (e.g 11106, index 5 means we would be out of the digits, so i-1 to get "6")
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        
        return dp[length]