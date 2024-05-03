class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1

        while left <= right and top <= bottom:
            # From left to right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1 # Lower top boundary down

            # From top to bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1 # Shrink right boundary to left

            # At this point, we may not have any rows left, so check
                # E.g. could have just been 1 row
            if top <= bottom: # Top has not crossed the bottom boundary
                # Go right to left, reverse
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1 # Expand bottom boundary to top
            
            if left <= right: # Left has not crossed right boundary
                # Go bottom top top
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1 # Expand left boundary to right
        
        return res

