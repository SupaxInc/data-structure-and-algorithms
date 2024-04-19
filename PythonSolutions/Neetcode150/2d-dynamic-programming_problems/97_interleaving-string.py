class BruteForceSolution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def dfs(s1, s2, s3):
            # Base case 1: All strings are empty, so we were able to interleave strings
            if not s1 and not s2 and not s3:
                return True
            # Base case 2: No longer valid if the lengths don't add up to s3
            if len(s1) + len(s2) != len(s3):
                return False
            
            # Choice 1: Use a char from s1, if it matches s3
                # Slice string by moving it over by 1
            useS1 = s1 and s1[0] == s3[0] and dfs(s1[1:], s2, s3[1:])
            # Choice 2: Use a char from s2
            useS2 = s2 and s2[0] == s3[0] and dfs(s1, s2[1:], s3[1:])

            # Return either options to check if a valid combination was found
            return useS1 or useS2
        
        return dfs(s1, s2, s3)

class TopDownSolution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
                return False
        
        cache = {}

        def dfs(s1, s2, s3):
            if (s1, s2, s3) in cache:
                return cache[(s1, s2, s3)]
            # Base case 1: All strings are empty, so we were able to interleave strings
            if not s1 and not s2 and not s3:
                return True
            # Base case 2: No longer valid if the lengths don't add up to s3
            if len(s1) + len(s2) != len(s3):
                return False
            
            # Choice 1: Use a char from s1, if it matches s3
                # Slice string by moving it over by 1
            useS1 = s1 and s1[0] == s3[0] and dfs(s1[1:], s2, s3[1:])
            # Choice 2: Use a char from s2
            useS2 = s2 and s2[0] == s3[0] and dfs(s1, s2[1:], s3[1:])

            cache[(s1, s2, s3)] = useS1 or useS2
            # Return either options to check if a valid combination was found
            return cache[(s1, s2, s3)]
        
        return dfs(s1, s2, s3)

class BottomUpSolution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        # If the lengths don't sum to s3's length, interleaving isn't possible
        if l1 + l2 != l3:
            return False

        # Create a DP table with dimensions (l1+1) x (l2+1)
        dp = [[False] * (l2 + 1) for _ in range(l1 + 1)]
        dp[0][0] = True  # Interleaving two empty strings should result in an empty string

        # Initialize the first column, checking if only s1 can form the prefix of s3
        for i in range(1, l1 + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]

        # Initialize the first row, checking if only s2 can form the prefix of s3
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
