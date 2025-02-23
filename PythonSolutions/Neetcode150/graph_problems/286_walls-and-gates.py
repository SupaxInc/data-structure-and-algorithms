class Solution:
    # *Don't have premium leetcode so this is using Islands and Treasure from Neetcode: https://neetcode.io/problems/islands-and-treasure*
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.grid = grid
        self.ROWS, self.COLS = len(grid), len(grid[0])
        self.DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        self.INF = 2**31 - 1
        queue = deque()

        for row in range(self.ROWS):
            for col in range(self.COLS):
                # Add each treasure chest to a queue so we can look for distance at the same time
                if self.grid[row][col] == 0:
                    queue.append((row, col))
                # Fill the land cells as INF since there may be land that can't be traversed
                elif self.grid[row][col] != -1:
                    self.grid[row][col] = self.INF
        
        self.levelOrderBFS(queue)
        
    def levelOrderBFS(self, queue):
        distance = 0
        
        while queue:
            levelSize = len(queue)
            # Increment the distance early since we don't count current level
            distance += 1

            for _ in range(levelSize):
                row, col = queue.popleft()

                # Check for cells in the NEXT level and not the current level
                # This is because we are counting the distance from the current level
                for dx, dy in self.DIRS:
                    newRow, newCol = row+dx, col+dy

                    # Base case 1: Boundary check
                    if newRow > self.ROWS-1 or newCol > self.COLS-1 or newRow < 0 or newCol < 0:
                        continue
                    
                    # Base case 2: Not a land cell so we can't traverse
                    if self.grid[newRow][newCol] != self.INF:
                        continue

                    # Visit the cell and add the distance
                    self.grid[newRow][newCol] = distance

                    queue.append((newRow, newCol))
                