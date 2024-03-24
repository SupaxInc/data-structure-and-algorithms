class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.ROWS, self.COLS = len(grid), len(grid[0])
        fresh = 0
        queue = deque()

        # Find all fresh oranges and rotten oranges
        for row in range(0, self.ROWS):
            for col in range(0, self.COLS):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    queue.append((row, col))
        
        # Run a level order BFS on the queue of rotten oranges
            # This is because rotten oranges rot at the same time and there may be more than 1 rotten orange
        return self.levelOrderBFS(grid, queue, fresh)
    
    def levelOrderBFS(self, grid, queue, fresh):
        # If all oranges are already rotten then return 0 minutes
        if not fresh:
            return 0
        
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        minutes = -1 # Begin at -1 since it'll count the first traversal of a rotten orange

        while queue:
            for _ in range(0, len(queue)):
                row, col = queue.popleft()

                # Do the validations right away on the new row and col so we only add rotten oranges to the queue
                    # If we don't do validations right away, we may end up adding fresh oranges to the queue
                    # Then our level order traversal will incorrectly count the minutes up
                for rowDir, colDir in DIRS:
                    newRow = row + rowDir
                    newCol = col + colDir

                    if newRow < 0 or newCol < 0 or newRow > self.ROWS - 1 or newCol > self.COLS - 1:
                        continue
                    if grid[newRow][newCol] != 1:
                        continue
                    
                    fresh -= 1
                    grid[newRow][newCol] = 2

                    queue.append([newRow, newCol])
            
            minutes += 1

        return minutes if fresh == 0 else -1