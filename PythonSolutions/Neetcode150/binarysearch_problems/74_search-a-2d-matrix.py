class BruteForceSolution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) < 1:
            return False

        for i in range(0, len(matrix)):
            lo, hi = 0, len(matrix[i]) - 1

            while lo <= hi:
                if target > matrix[i][hi]:
                    break
                
                mid = lo + ((hi - lo) // 2)

                if matrix[i][mid] == target:
                    return True
                
                if  matrix[i][mid] > target:
                    hi = mid - 1
                elif matrix[i][mid] < target:
                    lo = mid + 1
        
        return False
    
class OptimizedSolution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Check if the rows or columns are empty
        if not matrix or not matrix[0]:
            return False
        
        # Get total rows and columns of the 2d matrix
        rows, cols = len(matrix), len(matrix[0])

        # Treat it as a 1d array, so the highest pointer is at the end of the 2d array
        lo, hi = 0, rows * cols - 1

        while lo <= hi:
            mid = lo + ((hi - lo) // 2) # Grab the mid idx within a "1d array"
            # Grab the (y, x) coordinates to get the value of a "1d array"
            midVal = matrix[mid // cols][mid % cols]

            if midVal == target:
                return True

            if midVal > target:
                hi = mid - 1
            elif midVal < target:
                lo = mid + 1

        return False
