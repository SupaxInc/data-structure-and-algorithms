class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if not n:
            return []
    
        cols = set()
        posDiags = set()
        negDiags = set()
        # Rows do not need a set since we know for sure we are just visiting 1 row per choice
            # Thus there would never be a Queen on the same row

        res = []
        # Create a n * n board
            # [['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]
        board = [["."] * n for i in range(n)]

        def backtrack(row):
            # Stop when we reach end of board
            if row == n:
                # ['....', '....', '....', '....']
                joinedBoard = ["".join(boardRow) for boardRow in board]
                res.append(joinedBoard)
                return
            
            # Go through all the choices per row
                # (n is number of rows since board is n*n)
            for col in range(n):
                # Prune search if a Queen can eliminate another Queen
                if (row + col) in posDiags or (row - col) in negDiags or col in cols:
                    continue
                
                # Inclusion choice: Place the queen
                board[row][col] = "Q"
                # Add where the Queen can eliminate another Queen
                posDiags.add(row+col)
                negDiags.add(row-col)
                cols.add(col)

                # Explore the choice further (Go to next row and explore the next col choices)
                backtrack(row + 1)

                # Exclusion choice: Remove the queen
                board[row][col] = "."
                posDiags.remove(row+col)
                negDiags.remove(row-col)
                cols.remove(col)
            
        backtrack(0)
        return res