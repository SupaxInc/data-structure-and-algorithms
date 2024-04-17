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