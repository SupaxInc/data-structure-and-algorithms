class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.ROWS, self.COLS = len(grid), len(grid[0])
        self.DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        fresh = 0
        queue = deque()

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.grid[row][col] == 1:
                    fresh += 1
                # Add rotten oranges to queue since the rotten oranges all begin rotting at the same time
                # This ensures that we count the minutes accurately
                elif self.grid[row][col] == 2:
                    queue.append((row, col))
        
        return self.levelOrderBFS(queue, fresh)
    
    def levelOrderBFS(self, queue, fresh):
        if fresh == 0:
            return 0
        
        minutes = -1 # Begin at -1 since it'll count the first traversal of a rotten orange

        while queue:
            levelSize = len(queue)

            for i in range(levelSize):
                row, col = queue.popleft()

                # Process the new cells ahead of time rather than processing in the current level
                # If we process in current level, it will incorrectly add minutes due to:
                # - Possibly adding new cells to process that are in the base cases for next iteration
                # - If the cells are incorrect to process it will still add to queue thus incorrectly increase minutes
                for dx, dy in self.DIRS:
                    newRow, newCol = row+dx, col+dy

                    # Base case 1: Boundary check
                    if newRow > self.ROWS-1 or newCol > self.COLS-1 or newRow < 0 or newCol < 0:
                        continue
                    
                    # Base case 2: Check if the cell is already a rotten orange or is an empty cell
                    if self.grid[newRow][newCol] != 1:
                        continue
                    
                    # Visit the cell
                    self.grid[newRow][newCol] = 2 # Turns into a rotten orange
                    fresh -= 1

                    # Add the new cell to the queue
                    queue.append((newRow, newCol))
                
            minutes += 1
    
        return minutes if fresh == 0 else -1