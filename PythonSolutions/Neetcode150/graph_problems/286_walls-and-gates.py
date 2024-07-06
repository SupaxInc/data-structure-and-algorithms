class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2**31 - 1
        queue = deque([])

        # Traverse the grid and create the necesary INF land values along with adding treasure chests to queue
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row, col))
                elif grid[row][col] != -1:
                    grid[row][col] = INF
        
        DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        dist = 0

        # Level order traversal, begin at the treasure chests at the same time
        while queue:
            levelSize = len(queue)
            dist += 1
            
            for _ in range(levelSize):
                row, col = queue.popleft()

                for dx, dy in DIRS:
                    newRow, newCol = row + dx, col + dy

                    # Check if the new traversed grid is valid
                    if 0 <= newRow < ROWS and 0 <= newCol < COLS:
                        # If its a land value add the distance then append the grid so it can be traversed next level
                        if grid[newRow][newCol] == INF:
                            grid[newRow][newCol] = dist
                            queue.append((newRow, newCol))