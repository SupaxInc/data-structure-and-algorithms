class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        # E.g. n=4, [["...."], ["...."], ["...."], ["...."]]
        board = [["."] * n for i in range(n)]

        posDiag = set()
        negDiag = set()
        cols = set()
        
        # Explore each *row* options
        def backtrack(row):
            # Base case: Our reach is at the end of the board, no more options left
            if row == n:
                # E.g. [[".Q..","...Q","Q...","..Q."]]
                joinedBoard = ["".join(boardRow) for boardRow in board]
                res.append(joinedBoard)
                # Prune the search, no need to look for anymore options
                return
            
            # Traverse each *col* choices
            for col in range(n):
                # Prune the search if there is an existing queen that can eliminate the new position
                if (row+col) in posDiag or (row-col) in negDiag or col in cols:
                    continue
                
                # Inclusion choice: Place the queen
                board[row][col] = "Q"
                # Add the positions where the queen can now eliminate on the board
                posDiag.add(row+col)
                negDiag.add(row-col)
                cols.add(col)

                # Explore the choice deeper with different row options
                backtrack(row + 1)

                # Exclusion choice: Remove the queen and try other col choices
                board[row][col] = "."
                # Remove the positions of elimination since placed queen is gone
                posDiag.remove(row+col)
                negDiag.remove(row-col)
                cols.remove(col)


        backtrack(0)
        return res