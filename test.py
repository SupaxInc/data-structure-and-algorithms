def numDecodings(s: str) -> int:
    # Return 0 if the string is empty or starts with '0' because it can't be decoded.
    if not s or s[0] == '0':
        return 0

    n = len(s)  # Length of the input string
    dp = [0] * (n + 1)  # DP array to store the number of ways to decode up to each index
    dp[0], dp[1] = 1, 1  # Base cases: dp[0] is 1 because there's 1 way to decode an empty string, dp[1] is 1 if the first character is not '0'

    # Start filling the dp array from index 2 to n
    for i in range(2, n + 1):
        p = s[i-1]
        t = s[i-2]
        # If the current character is not '0', it can be decoded on its own,
        # so we add the number of ways to decode the string up to the previous character.
        if s[i-1] != '0':
            dp[i] += dp[i-1]
        
        # If the two characters at positions i-2 and i-1 form a number between 10 and 26,
        # they can be decoded together. We add the number of ways to decode the string
        # up to two characters before the current one.
        if 10 <= int(s[i-2:i]) <= 26:
            dp[i] += dp[i-2]

    # The last element in dp contains the total number of ways to decode the entire string.
    return dp[n]


numDecodings("123")