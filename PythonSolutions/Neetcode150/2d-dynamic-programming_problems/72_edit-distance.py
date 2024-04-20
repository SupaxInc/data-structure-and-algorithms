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