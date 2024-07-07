class CleanerSolution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.ROWS, self.COLS = len(board), len(board[0])
        self.board = board
        self.DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        # Capture regions that ARE NOT surrounded
            # Regions that are on the edges of the board can never be surrounded, so we need to capture it temporarily
            # Makes it easier to capture surrounded regions later since they are no longer "O"'s
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.board[row][col] == "O" and (row in [0, self.ROWS - 1] or col in [0, self.COLS - 1]):
                    # Do DFS on the edges since if a region is connected to a region on the edge
                    # It could no longer be captured as well
                    self.dfs(row, col)

        # Capture regions that ARE surrounded
            # We are able to just capture ALL regions now since they would all be surrounded
            # As we've captured all regions that can't be surrounded
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.board[row][col] == "O": # Regions that aren't surrounded are "TEMP"s
                    self.board[row][col] = "X"
        
        # Remove the capture on regions that ARE NOT surrounded
            # This is needed so that our board has the correct information of regions that are not surrounded
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.board[row][col] == "TEMP":
                    self.board[row][col] = "O"
        
    def dfs(self, row, col):
        # Boundary check
        if row > self.ROWS - 1 or col > self.COLS - 1 or row < 0 or col < 0:
            return
        
        # Valid check, if its no longer a region (could be temp or an X)
        if self.board[row][col] != "O":
            return
        
        # Convert regions to a temp so it could no longer be captured later
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