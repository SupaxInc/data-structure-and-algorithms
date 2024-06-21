class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        self.word, self.board = word, board
        self.rows, self.cols = len(board), len(board[0])

        # Count the frequencies of the letters for the board
            # Creates a counter for the letters for each row
            # Sums the counters for each row
            # Creates a dictionary using the summed counters as the initialization
        count = defaultdict(int, sum(map(Counter, board), Counter()))

        # Reverse the target word if the board's freq of first letter is more than freq of last letter
            # Helps lead quicker pruning of invalid paths
            # Since we will end up traversing to more paths if the first letter is shown more
        if count[word[0]] > count[word[-1]]:
            self.word = self.word[::-1]
    
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                # DFS each letter on the board
                    # Begin with the first index of the word (either reversed or not)
                if self.backtrack(row, col, 0):
                    return True
    
        return False

    # currIndex is the index we are currently on for the word we are searching for
    def backtrack(self, row, col, currIndex):
        # Stop if we find the word
        if currIndex == len(self.word):
            return True
        
        # Prune search if we hit boundaries
        if row > self.rows-1 or col > self.cols-1 or col < 0 or row < 0:
            return False

        # Prune search if current letter doesn't match the word letters, or if we visited node before
        if self.board[row][col] != self.word[currIndex] or self.board[row][col] == "":
            return False
        
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        # Visit node (inclusion)
        self.board[row][col] = ""

        # Travel to left, right, up, or down (explore)
        for rowDir, colDir in dirs:
            # Explore as deep as possible for one of direction choices
                # We are ONLY EXPLORING if the letter we are on matches the curr index (see prune search criterias above)
            if self.backtrack(row+rowDir, col+colDir, currIndex + 1):
                # Pop the call stacks if we end up finding the word
                return True
        
        # Unvisit node so add original letter (exclusion)
            # Exclusion after traversal since at this point the letter we are on matches the current index
            # Therefore, we have visited the node (inclusion), so we need to replace it back with current index we are on
        self.board[row][col] = self.word[currIndex]

        return False
            