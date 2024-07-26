class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        maxHeight = grid[0][0]
        # Heap to select the most minimum height in elevation levels first
            # Begin at the top left corner of the grid which is current max height/time
        minHeap = [(maxHeight, 0, 0)] # (max time/height, row, column)

        # Add the first row, column to set since we will process cells in the next cell over
        visited = set((0,0))

        while minHeap:
            currMaxTime, row, col = heapq.heappop(minHeap)

            # If we are in the bottom right corner return the max time
            if row == ROWS - 1 and col == COLS - 1:
                return currMaxTime

            for dr, dc in DIRS:
                newRow, newCol = row+dr, col+dc
                # Processing cells next cell over
                if newRow > ROWS - 1 or newCol > COLS - 1 or newRow < 0 or newCol < 0:
                    continue
                if (newRow, newCol) in visited:
                    continue
                
                visited.add((newRow, newCol))
                # Our max time is measured based on the highest elevation in our path 
                    # Because we have to wait for the elevation to rise (rain to fall) before we swim to the cell
                    # IF the next cells is smaller than our max height, we don't have to wait for time to pass
                    # Therefore, the highest elevation in our path is our max time
                heapq.heappush(minHeap, (max(currMaxTime, grid[newRow][newCol]), newRow, newCol))
        
        return maxHeight # This should never be reached
