class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) # Rule 1: Each row must contain the digits 1-9 without repetition.
        cols = defaultdict(set) # Rule 2: Each column must contain the digits 1-9 without repetition.
        squares = defaultdict(set) # Rule 3: Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

        # Iterate through each row [[], [], [], etc..]
        for r in range(0, len(board)):
            # iterate through the columns in each row [[., ., ., etc..]]
            for c in range(0, len(board[r])):
                value = board[r][c]
                
                # Checks if the value is anywhere within a certain 3x3 square out of the 9 squares
                squareKey = (r//3, c//3) 
                
                # Check if any of the rules are broken where 1-9 is found as duplicate
                if value in rows[r] or value in cols[c] or value in squares[squareKey]:
                    return False
                if value != ".":
                    # This will add all nums that belongs one of the rows
                    rows[r].add(value)
                    # This will add all nums that belongs to one of the columns
                    cols[c].add(value)
                    # This will add all nums that belongs to one of the 3x3 squares
                        # E.g. (2//3, 5//3) = (0, 1) = coords belongs to square 1, so we add all nums that are in square 1
                    squares[squareKey].add(value)
        
        return True