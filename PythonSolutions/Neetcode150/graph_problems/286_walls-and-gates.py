class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.ROWS, self.COLS = len(grid), len(grid[0])
        INF = 2**31 - 1
        queue = deque()
        
        # Initialize the grid: set INF for traversable land cells, identify treasure chests
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if grid[row][col] == 0:
                    queue.append((row, col, 0))  # Append treasure chests with initial distance 0
                elif grid[row][col] != -1:
                    grid[row][col] = INF  # Mark traversable land cells as INF

        # Directions: up, down, left, right
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Perform BFS from all treasure chests
        while queue:
            row, col, dist = queue.popleft()
            
            for rowDir, colDir in DIRS:
                newRow, newCol = row + rowDir, col + colDir
                
                if 0 <= newRow < self.ROWS and 0 <= newCol < self.COLS:
                    if grid[newRow][newCol] == INF:  # Update INF cells only
                        grid[newRow][newCol] = dist + 1
                        queue.append((newRow, newCol, dist + 1))
        
        # Note: There's no need to return grid as we're modifying it in place