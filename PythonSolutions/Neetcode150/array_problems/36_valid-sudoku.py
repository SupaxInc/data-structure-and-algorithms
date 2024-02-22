class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        # Iterate through each row [[], [], [], etc..]
        for r in range(0, len(board)):
            # iterate through the columns in each row [[., ., ., etc..]]
            for c in range(0, len(board[r])):
                value = board[r][c]
                
                # Checks if the value is anywhere within a certain 3x3 square out of the 9 squares
                squareKey = (r//3, c//3) 
                
                if value in rows[r] or value in cols[c] or value in squares[squareKey]:
                    return False
                if value != ".":
                    rows[r].add(value)
                    cols[c].add(value)
                    squares[squareKey].add(value) # This will add all values that pertains to one of the 3x3 squares
        
        return True