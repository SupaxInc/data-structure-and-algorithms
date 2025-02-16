class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board, self.word = board, word
        self.DIRS = [(0,1), (1, 0), (-1, 0), (0, -1)]
        self.COLS, self.ROWS = len(board[0]), len(board)

        # Count the number of letter 
            # map(Counter, board) -> An array of counters for each row on the board
            # sum(map, Counter()) -> Sums all counters into one counter
            # defaultdict(int, sum) -> Places the summed counter as a default dict to be used as one dictionary
        count = defaultdict(int, sum(map(Counter, board), Counter()))

        # Optimization:
            # Check if the beginning of the target word has more occurences on the board than the end of the word
        if count[word[0]] > count[word[-1]]:
            # Reverse the word so that we trigger less DFS's on the board since the end of the word has less occurences
            self.word = word[::-1]
        
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.dfs(row, col, 0):
                    return True
        
        return False
    
    def dfs(self, row, col, currIdx):
        # Base case 1: Word is found
        if len(self.word) == currIdx:
            return True

        # Base case 2: Boundary check
        if row > self.ROWS-1 or col > self.COLS-1 or row < 0 or col < 0:
            return False

        # Base case 3: Already visited or not part of the target word check
        if self.board[row][col] == "" or self.board[row][col] != self.word[currIdx]:
            return False
        
        # Visit the cell
        self.board[row][col] = ""
        
        # Explore the current choice deeper
        for dx, dy in self.DIRS:
            # Increase word index here instead of when visitng the cell so that we can backtrack when we unvisit later
            if self.dfs(row + dx, col + dy, currIdx + 1):
                # Return True if word has been found
                return True
        
        # Unvisit the cell (backtrack if the current choice had no valid paths)
        self.board[row][col] = self.word[currIdx]
        
        # Return false since there were no valid paths and word has not been found
        return False
