class CleanerSolution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.ROWS, self.COLS = len(board), len(board[0])
        self.DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        # 1) Convert O's in the boundary as temp
        for row in range(self.ROWS):
            for col in range(self.COLS):
                # - Check if row is in top or bottom, and if col is in left or right boundaries
                # - Check if the region is an "O" cell
                if (row in [0, self.ROWS-1] or col in [0, self.COLS-1]) and self.board[row][col] == "O":
                    # Run the DFS on the "O" in the boundary 
                    # since ANY region touching this "O" will no longer able to be surrounded by "X"'s
                    self.dfs(row, col)
        
        # 2) Convert O's not in the boundary as X's
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.board[row][col] == "O":
                    self.board[row][col] = "X"
        
        # 3) Convert temps back to O's
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.board[row][col] == "TEMP":
                    self.board[row][col] = "O"
    
    def dfs(self, row, col):
        # Base case 1: Boundary check
        if row > self.ROWS-1 or col > self.COLS-1 or row < 0 or col < 0:
            return
        
        # Base case 2: Visited check and if its not an "O" don't change it to TEMP 
        if self.board[row][col] != "O":
            return
        
        # Visit the cell
        self.board[row][col] = "TEMP"

        for dx, dy in self.DIRS:
            self.dfs(row+dx, col+dy)

        return

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.ROWS, self.COLS = len(board), len(board[0])

        # Capture unsurrounding regions: Border "O" -> "temp"
            # This should capture even "O"'s outside of the border if they are directionally attached
        for row in range(0, self.ROWS):
            for col in range(0, self.COLS):
                # Check if were on the border (e.g. r in [0, ROWS-1] means if were on 1st row or last row)
                if board[row][col] == "O" and (row in [0, self.ROWS - 1] or col in [0, self.COLS-1]):
                    self.capture(board, row, col)
        
        # Capture surrounded regions: "O" -> "X"
            # No need to DFS/BFS since all "O"'s left should be surrounded now
        for row in range(0, self.ROWS):
            for col in range(0, self.COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"


        # Uncapture unsurrounded regions: "temp" -> "O"
        for row in range(0, self.ROWS):
            for col in range(0, self.COLS):
                if board[row][col] == "temp":
                    board[row][col] = "O"

    def capture(self, board, row, col):
        if row < 0 or col < 0 or row > self.ROWS-1 or col > self.COLS-1:
            return
        
        if board[row][col] != "O":
            return
        
        board[row][col] = "temp"
        self.capture(board, row + 1, col)
        self.capture(board, row, col + 1)
        self.capture(board, row - 1, col)
        self.capture(board, row, col - 1)