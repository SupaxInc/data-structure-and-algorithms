from typing import List
class CleanerSolution:
    def solve(self, board: List[List[str]]) -> None:
        self.ROWS, self.COLS = len(board), len(board[0])
        self.DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        borderRows = set([0, self.ROWS - 1])
        borderCols = set([0, self.COLS - 1])

        # Mark boundaries as "TEMP", DFS so we mark all cells that are attached to a boundary
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if (row in borderRows or col in borderCols) and board[row][col] == "O":
                    # Any "O"s attached to a boundary can no longer be surrounded
                    self.dfs(row, col, board)
        
        # Convert any O's that are not connected to a boundary as surrounded "X"
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"
        
        # Convert the "TEMP" boundary cells back to an unsurrounded "O"
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if board[row][col] == "TEMP":
                    board[row][col] = "O"
    
    def dfs(self, row, col, board):
        # Base case: Cell has already been visited
        if board[row][col] == "TEMP":
            return
        
        board[row][col] = "TEMP"

        for dx, dy in self.DIRS:
            nr, nc = row + dx, col + dy

            if nr < 0 or nc < 0 or nr > self.ROWS - 1 or nc > self.COLS - 1:
                continue
            
            if board[nr][nc] == "X":
                continue
            
            self.dfs(nr, nc, board)
        
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