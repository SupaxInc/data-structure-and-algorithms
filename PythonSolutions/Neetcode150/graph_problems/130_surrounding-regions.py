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