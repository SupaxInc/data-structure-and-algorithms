def isInterleave(s1, s2, s3):
    l1, l2, l3 = len(s1), len(s2), len(s3)
    # If the lengths don't sum to s3's length, interleaving isn't possible
    if l1 + l2 != l3:
        return False

    # Create a DP table with dimensions (l1+1) x (l2+1)
    dp = [[False] * (l2 + 1) for _ in range(l1 + 1)]
    dp[0][0] = True  # Interleaving two empty strings should result in an empty string

    # Initialize the first row, checking if only s1 can form the prefix of s3
    for i in range(1, l1 + 1):
        dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]

    # Initialize the first column, checking if only s2 can form the prefix of s3
    for j in range(1, l2 + 1):
        dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

    # Fill the rest of the dp table
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            # Check if the current character of s3 can be formed by the current character of s1
            from_s1 = dp[i-1][j] and s1[i-1] == s3[i+j-1]
            # Check if the current character of s3 can be formed by the current character of s2
            from_s2 = dp[i][j-1] and s2[j-1] == s3[i+j-1]

            # Update the dp table at position (i, j)
            dp[i][j] = from_s1 or from_s2

    # The bottom-right value in the dp table will tell if s3 can be fully interleaved by s1 and s2
    return dp[l1][l2]

# Example usage
s1 = "abc"
s2 = "def"
s3 = "adbcef"
print(isInterleave(s1, s2, s3))  # Output: True
