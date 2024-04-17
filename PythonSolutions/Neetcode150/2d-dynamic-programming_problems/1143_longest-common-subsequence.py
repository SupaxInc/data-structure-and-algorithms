class BruteForceSolution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def dfs(i, j):
            # Base case: Hitting boundary
            if i == len(text1) or j == len(text2):
                return 0
            # Choice 1: Letters match, move to next character
            if text1[i] == text2[j]:
                return 1 + dfs(i + 1, j + 1)
            # Choice 2: Letters don't match, skip the character from text1 or text2
            else:
                return max(dfs(i + 1, j), dfs(i, j + 1))
        
        return dfs(0, 0)
    
class MemoizedSolution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}

        def dfs(i, j):
            # Base case: Already in cache
            if (i, j) in cache:
                return cache[(i, j)]
            # Base case: Hitting boundary
            if i == len(text1) or j == len(text2):
                return 0

            # Choice 1: Letters match, move to next character
            if text1[i] == text2[j]:
                cache[(i, j)] = 1 + dfs(i + 1, j + 1)
            # Choice 2: Letters don't match, skip the character from text1 or text2
            else:
                cache[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))
            
            return cache[i, j]
        
        return dfs(0, 0)

class BottomUpSolution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # Fill 2D matrix with 0's
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Pretend we flipped and inverted the 2d matrix from the bottom up approach
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Choice 1: Matches, calculate diagonally (move to next letters for both text1 or text2)
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                # Choice 2: Does not match, choose from top or left (skip character from text1 or text2)
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Bottom right cell contains LCS
        return dp[m][n]