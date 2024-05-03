class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        # Check if the first rows and columns had zeros initially
            # This is important since we can lose track when we start setting zeros
            # for our first row and col tracker. If we lose track, then these columns wont be marked with zeros
        first_row_has_zeros = any(matrix[0][j] == 0 for j in range(COLS))
        first_col_has_zeros = any(matrix[i][0] == 0 for i in range(ROWS))
        
        # Begin marking our first row and col trackers as zeros
            # Lets us figure out if the whole row and column needs to be set as 0
        for i in range(1, ROWS):
            for j in range(1, COLS):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0 # Mark first column as 0
                    matrix[i][0] = 0 # Mark first row as 0
        
        # Starting setting the rows and columns as zeros based on the trackers
        for i in range(1, ROWS):
            for j in range(1, COLS):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        # Set the first row's zeros if there were initial zeros
        if first_row_has_zeros:
            for j in range(COLS):
                matrix[0][j] = 0
        
        # Set the first col's zeros if there were initial zeros
        if first_col_has_zeros:
            for i in range(ROWS):
                matrix[i][0] = 0