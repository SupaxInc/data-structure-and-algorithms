class BruteForceSolution:
    def minDistance(self, word1: str, word2: str) -> int:
        def dfs(i, j):
            # Base case 1: Both words are empty or became empty
            if i == len(word1) and j == len(word2):
                return 0
            # Base case 2: Reached end of word 1, could be too much deletion
                # Insert the rest of the characters to reach word 2
            if i == len(word1):
                return len(word2) - j
            # Base case 3: Reached end of word 2, could be too much insertion
            if j == len(word2):
                return len(word1) - i

            
            # Letters match so no operation
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            else:
                insertion = 1 + dfs(i, j + 1)
                deletion = 1 + dfs(i + 1, j)
                # Similar to a matched letter since we are forcing the letters to match
                replace = 1 + dfs(i + 1, j + 1) 
            
            return min(insertion, deletion, replace)

        return dfs(0, 0)

class TopDownSolution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            # Base case 1: Both words are empty or became empty
            if i == len(word1) and j == len(word2):
                return 0
            # Base case 2: Reached end of word 1, could be too much deletion
                # Insert the rest of the characters to reach word 2
            if i == len(word1):
                return len(word2) - j
            # Base case 3: Reached end of word 2, could be too much insertion
            if j == len(word2):
                return len(word1) - i

            
            # Letters match so no operation
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            else:
                insertion = 1 + dfs(i, j + 1)
                deletion = 1 + dfs(i + 1, j)
                # Similar to a matched letter since we are forcing the letters to match
                replace = 1 + dfs(i + 1, j + 1) 
            
            cache[(i, j)] = min(insertion, deletion, replace)
            return cache[(i, j)]

        return dfs(0, 0)
    
class BottomUpSolution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # Create a DP table with dimensions (m+1) x (n+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Initialize the first column: transforming the first i characters of word1 into an empty word2
        for i in range(1, m + 1):
            dp[i][0] = i  # Requires i deletions

        # Initialize the first row: transforming an empty word1 into the first j characters of word2
        for j in range(1, n + 1):
            dp[0][j] = j  # Requires j insertions

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Check if the current characters are the same
                if word1[i-1] == word2[j-1]:
                    # If the characters match, the edit distance does not increase
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # Calculate costs for each possible operation:
                    # 1. Insertion: insert word2[j-1] into word1 at position i
                    # 2. Deletion: delete character word1[i-1]
                    # 3. Substitution: replace word1[i-1] with word2[j-1]
                    dp[i][j] = 1 + min(
                        dp[i][j-1],    # Insertion
                        dp[i-1][j],    # Deletion
                        dp[i-1][j-1]   # Substitution
                    )

        # The element at dp[m][n] contains the minimum edit distance
        return dp[m][n]